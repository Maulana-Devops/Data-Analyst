from __future__ import annotations

from typing import Callable, Sequence

import plotly.graph_objects as go

from src.formatting import format_rupiah

PRIMARY_COLOR = "#2E5A87"
SECONDARY_COLOR = "#C77700"
NEUTRAL_COLOR = "#6B7280"


def empty_figure(message: str = "Tidak ada data pada filter saat ini.") -> go.Figure:
    fig = go.Figure()
    fig.add_annotation(
        text=message,
        x=0.5,
        y=0.5,
        xref="paper",
        yref="paper",
        showarrow=False,
        font=dict(color="#6B7280", size=13),
    )
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    fig.update_layout(height=320, margin=dict(l=10, r=10, t=40, b=10))
    return fig


def bar_chart(
    labels: Sequence,
    values: Sequence,
    *,
    title: str,
    category_title: str,
    value_title: str,
    value_formatter: Callable[[float], str] = format_rupiah,
    orientation: str = "v",
    color: str = PRIMARY_COLOR,
    height: int = 420,
) -> go.Figure:
    labels = list(labels)
    values = list(values)
    if not labels:
        return empty_figure()

    texts = [value_formatter(value) for value in values]
    if orientation == "h":
        fig = go.Figure(
            go.Bar(
                x=values,
                y=labels,
                orientation="h",
                marker_color=color,
                text=texts,
                textposition="outside",
                cliponaxis=False,
            )
        )
        fig.update_xaxes(title_text=value_title)
        fig.update_yaxes(title_text=category_title, autorange="reversed")
    else:
        fig = go.Figure(
            go.Bar(
                x=labels,
                y=values,
                marker_color=color,
                text=texts,
                textposition="outside",
                cliponaxis=False,
            )
        )
        fig.update_xaxes(title_text=category_title)
        fig.update_yaxes(title_text=value_title)

    fig.update_layout(
        title=title,
        height=height,
        margin=dict(l=10, r=10, t=60, b=10),
    )
    return fig


def grouped_bar_chart(
    labels: Sequence,
    series: dict[str, Sequence],
    *,
    title: str,
    category_title: str,
    value_title: str,
    value_formatter: Callable[[float], str] = format_rupiah,
    colors: Sequence[str] | None = None,
    height: int = 420,
) -> go.Figure:
    labels = list(labels)
    if not labels or not series:
        return empty_figure()

    palette = list(colors) if colors else [PRIMARY_COLOR, SECONDARY_COLOR, NEUTRAL_COLOR]
    fig = go.Figure()
    for index, (name, values) in enumerate(series.items()):
        texts = [value_formatter(value) for value in values]
        fig.add_trace(
            go.Bar(
                name=name,
                x=labels,
                y=list(values),
                marker_color=palette[index % len(palette)],
                text=texts,
                textposition="outside",
                cliponaxis=False,
            )
        )

    fig.update_layout(
        title=title,
        barmode="group",
        height=height,
        margin=dict(l=10, r=10, t=60, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    fig.update_xaxes(title_text=category_title)
    fig.update_yaxes(title_text=value_title)
    return fig
