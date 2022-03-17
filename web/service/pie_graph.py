from datetime import datetime

import plotly.graph_objs as go
from django.db.models import Count
from django_registration.forms import User
from plotly.offline import plot

from web.mood_colors import COLORS
from web.service.base_graph import BaseGraph

PERIODS = ["mood_day", "mood_night"]


class PieGraphService(BaseGraph):
    def __init__(
        self, user: User, mood_mapping: dict, start_dt: datetime, end_dt: datetime
    ):
        super().__init__(start_dt=start_dt, end_dt=end_dt)
        self.user = user
        self.mood_mapping = mood_mapping

    def build_chart(self, period: str) -> str:
        label_numbers, values = self.load_data(period)
        labels = [self.mood_mapping.get(x) for x in label_numbers]
        colors = [COLORS[x] for x in label_numbers]
        fig = go.Figure(
            data=[
                go.Pie(
                    labels=labels,
                    values=values,
                    textinfo="label+percent",
                    insidetextorientation="radial",
                    marker=dict(colors=colors, line=dict(color="#000000", width=2)),
                )
            ]
        )
        return plot(fig, output_type="div", include_plotlyjs=True)

    def load_data(self, period: str):
        if period not in PERIODS:
            raise ValueError(f"period must be one of {PERIODS}")
        qs = (
            self.date_range_qs()
            .values(period)
            .annotate(total=Count(period))
            .order_by("total")
        )
        labels = []
        values = []
        for item in qs:
            if not item[period]:
                continue
            labels.append(item[period])
            values.append(item["total"])
        return labels, values
