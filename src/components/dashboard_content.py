import flet as ft
from src.components.glass_container import create_glass_card

def build_dashboard() -> ft.Stack:
    # Criamos um Stack (quadro) onde os cards podem ficar soltos
    dashboard_area = ft.Stack(expand=True)

    # Função que transforma qualquer container num card arrastável
    def make_draggable_card(content, top, left, width, height):
        card = create_glass_card(content=content, width=width, height=height)
        card.top = top
        card.left = left

        # Lógica de arrastar
        def on_pan_update(e: ft.DragUpdateEvent):
            card.top = max(0, (card.top or 0) + e.delta_y)
            card.left = max(0, (card.left or 0) + e.delta_x)
            card.update()

        return ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.MOVE, # Muda o cursor para "mover"
            drag_interval=10,
            on_pan_update=on_pan_update,
            content=card
        )

    # --- CONTEÚDO DOS CARDS (SEM EMOJIS, COM ÍCONES) ---

    # Card 1: Progresso
    card_progresso = make_draggable_card(
        content=ft.Column([
            ft.Row([ft.Icon(ft.Icons.INSIGHTS, color=ft.Colors.PURPLE_300), ft.Text("Seu progresso", weight=ft.FontWeight.BOLD)]),
            ft.Row([
                ft.ProgressRing(value=0.72, width=80, height=80, stroke_width=8, color=ft.Colors.PURPLE_300),
                ft.Column([
                    ft.Checkbox(label="Revisar requisitos", value=True),
                    ft.Checkbox(label="Concluir Spring Boot", value=False),
                ], spacing=5),
            ], spacing=20)
        ]),
        top=20, left=0, width=350, height=180
    )

    # Card 2: Mercado
    card_mercado = make_draggable_card(
        content=ft.Column([
            ft.Row([ft.Icon(ft.Icons.BAR_CHART, color=ft.Colors.GREEN_300), ft.Text("O mercado em números", weight=ft.FontWeight.BOLD)]),
            ft.Row([
                ft.Column([ft.Text("1.2k", size=30, weight=ft.FontWeight.BOLD), ft.Text("vagas analisadas", size=12, color=ft.Colors.WHITE_54)]),
                ft.Column([ft.Text("37", size=30, weight=ft.FontWeight.BOLD), ft.Text("novos requisitos", size=12, color=ft.Colors.WHITE_54)]),
            ], spacing=40),
        ]),
        top=20, left=370, width=350, height=180
    )

    # Card 3: Carreiras
    card_carreiras = make_draggable_card(
        content=ft.Column([
            ft.Row([ft.Icon(ft.Icons.WORK, color=ft.Colors.BLUE_300), ft.Text("Suas carreiras", weight=ft.FontWeight.BOLD), ft.Text("Ver todos", size=12, color=ft.Colors.PURPLE_300)]),
            ft.ListTile(leading=ft.Icon(ft.Icons.STAR, color=ft.Colors.YELLOW_300, size=18), title=ft.Text("Favoritos"), trailing=ft.Text("12")),
            ft.ListTile(leading=ft.Icon(ft.Icons.CIRCLE, color=ft.Colors.BLUE_300, size=14), title=ft.Text("Relevantes"), trailing=ft.Text("18")),
        ], spacing=0),
        top=220, left=0, width=350, height=220
    )

    # Card 4: Requisitos
    card_requisitos = make_draggable_card(
        content=ft.Column([
            ft.Row([ft.Icon(ft.Icons.LOCAL_FIRE_DEPARTMENT, color=ft.Colors.ORANGE_300), ft.Text("Requisitos exigidos", weight=ft.FontWeight.BOLD)]),
            ft.Text("Java", size=12),
            ft.ProgressBar(value=0.8, color=ft.Colors.PURPLE_300, bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.WHITE)),
            ft.Text("SQL", size=12),
            ft.ProgressBar(value=0.6, color=ft.Colors.PURPLE_300, bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.WHITE)),
        ], spacing=10),
        top=220, left=370, width=350, height=220
    )

    # Adicionando os cards ao quadro
    dashboard_area.controls.extend([
        card_progresso,
        card_mercado,
        card_carreiras,
        card_requisitos,
    ])

    return dashboard_area