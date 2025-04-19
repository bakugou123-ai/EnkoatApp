import asyncio
from asgiref.sync import sync_to_async
import nest_asyncio
import os
import django
from bokeh.models import Select, CustomJS


nest_asyncio.apply()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  # update with your project name
django.setup()

from app.models import Quote
import pandas as pd
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Select, DateRangeSlider,Div
from bokeh.layouts import column, row, gridplot
from bokeh.transform import dodge


@sync_to_async
def get_quotes():
    return list(Quote.objects.all().values())

async def load_data():
    quotes = await get_quotes()
    df = pd.DataFrame(quotes)
    df['project_date'] = pd.to_datetime(df['project_date'])
    return df

df = asyncio.run(load_data())  # ✅ Run async task synchronously

df['project_date'] = pd.to_datetime(df['project_date'])
state_group = df.groupby('project_state').size().reset_index(name="count")
avg_roof_by_type = df.groupby('roof_type')['roof_size'].mean().reset_index(name='avg_roof_size')

df['month'] = df['project_date'].dt.to_period('M').astype(str)
monthly_trend = df.groupby('month').size().reset_index(name='count')

total_projects = len(df)
avg_roof_size = round(df['roof_size'].mean(), 2)

source = ColumnDataSource(state_group)
source1 = ColumnDataSource(avg_roof_by_type)
source_month = ColumnDataSource(monthly_trend)
p1 = figure(x_range=state_group['project_state'], title="Projects by State", height=350)

p1.vbar(x='project_state',top='count',width=0.5,source=source)

p2 = figure(x_range=avg_roof_by_type['roof_type'], title="Average Roof Size by Roof Type", height=350)

p2.vbar(x='roof_type',top='avg_roof_size',width=0.5,source=source1)

p3 = figure(x_range=source_month.data['month'], title="Monthly Project Trend", height=350, x_axis_label="Month", x_axis_type="auto")
p3.line(x='month', y='count', source=source_month, line_width=2)
p3.circle(x='month', y='count', source=source_month, size=6)
p3.xaxis.major_label_orientation = 1.5708 

from bokeh.models import Button, CustomJS, Div

# 1. Create the summary div (hidden by default)
summary = Div(
    text=f"<b>Total Projects:</b> {total_projects} &nbsp; | &nbsp; <b>Average Roof Size:</b> {avg_roof_size} sq ft",
    css_classes=["summary-box"],
    visible=False
)

# 2. Create a toggle button to show/hide the summary
summary_button = Button(label="Show Summary", button_type="success", width=150)

# 3. Add interactivity with CustomJS (no server needed)
summary_button.js_on_click(CustomJS(args=dict(div=summary, btn=summary_button), code="""
    div.visible = !div.visible;
    btn.label = div.visible ? "Hide Summary" : "Show Summary";
"""))



layout = column(
    summary,
    summary_button,
    gridplot([
        [p1, p2],
        [p3, None]
    ], sizing_mode="fixed"),
    css_classes=["bk-root"])
curdoc().add_root(layout)






