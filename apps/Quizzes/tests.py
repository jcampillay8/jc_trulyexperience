from django.test import TestCase

# Create your tests here.



def serve_layout():  
    return dbc.Container(
    [
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row(dbc.Col(html.H1("Quiz_GCP - Digital Leader", className='text-center mb-4 '), width=12)),

        # Agrega las pestañas aquí
        dcc.Tabs(id="tabs-quiz", value='tab-1-quiz', children=[
            dcc.Tab(label='Quiz', value='tab-1-quiz', children=[
                # Mueve todo el layout existente aquí
                html.Div(id='question-index', style={'display': True}),
                dbc.Row(
                    [
                        dbc.Col(html.H4(id='question', className='text-center mb-4'), width=12),
                        dbc.Col(
                                    [
                                        dcc.Checklist(id='options', inputStyle={"margin-right": "20px"}),
                                    ],
                                    width={'size': 12, 'offset': 1},  
                                ),
                    ],
                    className='justify-content-center mb-4',
                ),
                dbc.Row(
                    [
                dbc.Col(
                    [
                        html.Button('Submit', id='submit', n_clicks=0, style={'background-color': 'blue', 'color': 'white'}, className='mx-2'),
                        html.Button('Next', id='next', n_clicks=0, style={'background-color': 'green', 'color': 'white'}, className='mx-2'),
                        html.Span("Filtro", className="mx-2"),  
                        dcc.Input(id='input_threshold', type='number', value=input_threshold, style={"width": "50px"}),  
                        html.Button("Explanation", id="open-explanation", style={'background-color': 'yellow', 'color': 'black'}, className='mx-2'),
                        html.Button("Reset Values", id="reset-values", style={'background-color': 'red', 'color': 'white'}, className='mx-2'), 
                    ],
                    width={'size': 6, 'offset': 1}, 
                ),
                dcc.ConfirmDialog(
                    id="confirm",
                    message="",
                ),
                dcc.ConfirmDialog(  
                id="confirm-reset",
                message="¿Seguro que desea resetar los valores?",
                ),
                            ],
                            className='justify-content-center',
                        ),
                        dbc.Col(html.Div(id='answer', className='text-center mt-4'), width={'size': 6, 'offset': 3}),
                dcc.Store(id='next_clicked', data=0),
            ]),
        dcc.Tab(label='Edit', value='tab-2-edit', children=[
            dcc.Textarea(id='edit-question-input', style={"width": "100%"}),
            html.Div(id='edit-options-inputs'),  # Contenedor para los campos de entrada de las opciones
            html.Button('Save', id='edit-save', n_clicks=0, style={'background-color': 'purple', 'color': 'white'}, className='mx-2'),
        ]),
        ]),
    ],
    fluid=True,
)

app.layout = serve_layout