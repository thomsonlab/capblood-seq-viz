from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from .. import figures


def add_gene_click_listener(app):

    @app.callback(
        Output("individuality_gene_dropdown", "value"),
        [
            Input("individuality_plot", "clickData")
        ]
    )
    def update_gene_dropdown(click_data):

        if click_data is None:
            raise PreventUpdate

        gene_name = click_data["points"][0]["text"]

        return gene_name


def add_gene_selected_listener(app):

    @app.callback(
        Output("individual_gene_mean_trace", "figure"),
        [
            Input("individuality_gene_dropdown", "value")
        ]
    )
    def update_gene_dropdown(gene):

        if gene is None:
            raise PreventUpdate

        return figures.individuality.get_gene_traces(gene)
