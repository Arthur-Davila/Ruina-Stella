import flet as ft
from src.components.glass_container import create_glass_card

def build_dashboard(page: ft.Page) -> ft.Stack:
    dashboard_area = ft.Stack(
        expand=True,
        fit=ft.StackFit.EXPAND,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )
    
    GRID_SIZE = 15
    grid_color = ft.Colors.with_opacity(0.08, ft.Colors.WHITE)

    # 1. GRID VISUAL
    dashboard_area.controls.extend(
        ft.Container(width=1, left=pos, top=0, bottom=0, bgcolor=grid_color)
        for pos in range(GRID_SIZE, 2000, GRID_SIZE)
    )
    dashboard_area.controls.extend(
        ft.Container(height=1, left=0, right=0, top=pos, bgcolor=grid_color)
        for pos in range(GRID_SIZE, 2000, GRID_SIZE)
    )

    all_cards = []
    dashboard_size = {"width": 0.0, "height": 0.0}

    def keep_cards_inside_dashboard(event: ft.LayoutSizeChangeEvent) -> None:
        dashboard_size["width"] = event.width
        dashboard_size["height"] = event.height

        for card in all_cards:
            card.width = min(card.width or 0, event.width)
            card.height = min(card.height or 0, event.height)
            card.left = min(max(card.left or 0, 0), event.width - (card.width or 0))
            card.top = min(max(card.top or 0, 0), event.height - (card.height or 0))

        dashboard_area.update()

    dashboard_area.on_size_change = keep_cards_inside_dashboard

    def make_draggable_resizable_card(content: ft.Control, top: int, left: int, width: int, height: int) -> ft.Container:
        
        card_bg = ft.Container(
            bgcolor=ft.Colors.with_opacity(0.4, "#09090b"),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.15, ft.Colors.WHITE)),
            border_radius=16,
            shadow=ft.BoxShadow(blur_radius=25, color=ft.Colors.with_opacity(0.6, ft.Colors.BLACK), offset=ft.Offset(0, 8)),
            expand=True
        )

        card_content = ft.Container(
            content=content,
            padding=20,
            expand=True,
        )

        pos_inicial = {"x": left, "y": top}

        def get_max_x() -> float: return dashboard_size["width"]
        def get_max_y() -> float: return dashboard_size["height"]

        # --- 1. LÓGICA DE MOVER (Arrastar pela borda superior) ---
        def on_drag_start(e: ft.DragStartEvent):
            pos_inicial["x"] = gesture_card.left
            pos_inicial["y"] = gesture_card.top

        def on_drag_update(event: ft.DragUpdateEvent) -> None:
            if event.local_delta:
                new_left = (gesture_card.left or 0) + event.local_delta.x
                new_top = (gesture_card.top or 0) + event.local_delta.y
                gesture_card.left = max(0, min(new_left, get_max_x() - (gesture_card.width or 0)))
                gesture_card.top = max(0, min(new_top, get_max_y() - (gesture_card.height or 0)))
                dashboard_area.update()

        def on_drag_end(event: ft.DragEndEvent) -> None:
            snapped_x = round((gesture_card.left or 0) / GRID_SIZE) * GRID_SIZE
            snapped_y = round((gesture_card.top or 0) / GRID_SIZE) * GRID_SIZE
            snapped_x = max(0, min(snapped_x, get_max_x() - (gesture_card.width or 0)))
            snapped_y = max(0, min(snapped_y, get_max_y() - (gesture_card.height or 0)))

            colidiu = False
            for other_card in all_cards:
                if other_card == gesture_card: continue
                if (snapped_x < (other_card.left or 0) + (other_card.width or 0) and
                    snapped_x + (gesture_card.width or 0) > (other_card.left or 0) and
                    snapped_y < (other_card.top or 0) + (other_card.height or 0) and
                    snapped_y + (gesture_card.height or 0) > (other_card.top or 0)):
                    colidiu = True
                    break

            if colidiu:
                gesture_card.left = pos_inicial["x"]
                gesture_card.top = pos_inicial["y"]
            else:
                gesture_card.left = snapped_x
                gesture_card.top = snapped_y
            dashboard_area.update()

        # --- 2. LÓGICA DE REDIMENSIONAR (Direita e Baixo) ---
        def on_resize_right_update(e: ft.DragUpdateEvent):
            if e.local_delta:
                max_w = max(0, get_max_x() - (gesture_card.left or 0))
                new_w = min(max(150, (gesture_card.width or 0) + e.local_delta.x), max_w)
                
                colidiu = False
                for other in all_cards:
                    if other == gesture_card: continue
                    if (gesture_card.left < (other.left or 0) + (other.width or 0) and
                        gesture_card.left + new_w > (other.left or 0) and
                        gesture_card.top < (other.top or 0) + (other.height or 0) and
                        gesture_card.top + (gesture_card.height or 0) > (other.top or 0)):
                        colidiu = True
                        break
                if not colidiu:
                    gesture_card.width = new_w
                    dashboard_area.update()

        def on_resize_bottom_update(e: ft.DragUpdateEvent):
            if e.local_delta:
                max_h = max(0, get_max_y() - (gesture_card.top or 0))
                new_h = min(max(100, (gesture_card.height or 0) + e.local_delta.y), max_h)
                
                colidiu = False
                for other in all_cards:
                    if other == gesture_card: continue
                    if (gesture_card.left < (other.left or 0) + (other.width or 0) and
                        gesture_card.left + (gesture_card.width or 0) > (other.left or 0) and
                        gesture_card.top < (other.top or 0) + (other.height or 0) and
                        gesture_card.top + new_h > (other.top or 0)):
                        colidiu = True
                        break
                if not colidiu:
                    gesture_card.height = new_h
                    dashboard_area.update()

        def on_resize_end(e: ft.DragEndEvent):
            gesture_card.width = max(150, round((gesture_card.width or 0) / GRID_SIZE) * GRID_SIZE)
            gesture_card.height = max(100, round((gesture_card.height or 0) / GRID_SIZE) * GRID_SIZE)
            dashboard_area.update()

        # --- 3. AS ALÇAS INVISÍVEIS ---
        # Borda Superior (Mover)
        drag_handle = ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.MOVE,
            on_pan_start=on_drag_start,
            on_pan_update=on_drag_update,
            on_pan_end=on_drag_end,
            top=0, left=0, right=0, height=25, # Faixa invisível no topo
            content=ft.Container(expand=True), # Necessário no Flet 1.x para o gesto funcionar
        )

        # Borda Direita (Alargar)
        resize_right_handle = ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.RESIZE_LEFT_RIGHT,
            on_pan_update=on_resize_right_update,
            on_pan_end=on_resize_end,
            right=0, top=25, bottom=0, width=15, # Faixa invisível na direita
            content=ft.Container(expand=True),
        )

        # Borda Inferior (Aumentar Altura)
        resize_bottom_handle = ft.GestureDetector(
            mouse_cursor=ft.MouseCursor.RESIZE_UP_DOWN,
            on_pan_update=on_resize_bottom_update,
            on_pan_end=on_resize_end,
            bottom=0, left=0, right=15, height=15, # Faixa invisível embaixo
            content=ft.Container(expand=True),
        )

        # Montando o card com o visual e as alças
        card_stack = ft.Stack([
            card_bg,
            card_content,
            drag_handle,
            resize_right_handle,
            resize_bottom_handle,
        ])

        # O Container externo que segura tudo
        gesture_card = ft.Container(
            left=left,
            top=top,
            width=width,
            height=height,
            content=card_stack,
        )

        all_cards.append(gesture_card)
        return gesture_card

    # --- DESIGN DOS CARDS ---
    card_progresso = ft.Column(
        [
            ft.Row([ft.Text("Seu progresso", weight=ft.FontWeight.BOLD, size=16), ft.Icon(ft.Icons.TRENDING_UP, size=16, color=ft.Colors.WHITE_54)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(color=ft.Colors.with_opacity(0.05, ft.Colors.WHITE), height=10),
            ft.Row(
                [
                    ft.Stack([ft.ProgressRing(value=0.72, width=80, height=80, stroke_width=8, color=ft.Colors.GREEN_300, bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.WHITE)), ft.Container(width=80, height=80, alignment=ft.Alignment.CENTER, content=ft.Text("72%", weight=ft.FontWeight.BOLD))]),
                    ft.Column(
                        [
                            ft.Checkbox(label="Revisar requisitos de Java", value=True, expand=True),
                            ft.Checkbox(label="Concluir curso de Spring Boot", value=False, expand=True),
                            ft.Checkbox(label="Atualizar currículo", value=False, expand=True)
                        ], 
                        spacing=0, 
                        expand=True 
                    )
                ],
                spacing=20,
                expand=True 
            )
        ],
        expand=True
    )

    card_mercado = ft.Column(
        [
            ft.Row([ft.Text("O mercado em números", weight=ft.FontWeight.BOLD, size=16), ft.Icon(ft.Icons.BAR_CHART, size=16, color=ft.Colors.WHITE_54)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(color=ft.Colors.with_opacity(0.05, ft.Colors.WHITE), height=10),
            ft.Row(
                [
                    ft.Column([ft.Text("1.2k", size=28, weight=ft.FontWeight.BOLD), ft.Text("vagas analisadas", size=12, color=ft.Colors.WHITE_54), ft.Text("↑ 12%", size=10, color=ft.Colors.GREEN_300)], spacing=2, expand=True),
                    ft.Column([ft.Text("37", size=28, weight=ft.FontWeight.BOLD), ft.Text("novos requisitos", size=12, color=ft.Colors.WHITE_54), ft.Text("↑ 8%", size=10, color=ft.Colors.GREEN_300)], spacing=2, expand=True),
                ],
                spacing=40,
                expand=True
            )
        ],
        expand=True
    )

    card_carreiras = ft.Column(
        [
            ft.Row([ft.Text("Suas carreiras", weight=ft.FontWeight.BOLD, size=16), ft.Text("Organizadas por IA", size=10, color=ft.Colors.WHITE_54)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(color=ft.Colors.with_opacity(0.05, ft.Colors.WHITE), height=10),
            ft.Row([ft.Icon(ft.Icons.STAR, size=16, color=ft.Colors.YELLOW_300), ft.Text("Favoritos", size=13, expand=True), ft.Text("12", size=13), ft.Icon(ft.Icons.CHEVRON_RIGHT, size=14, color=ft.Colors.WHITE_38)]),
            ft.Row([ft.Icon(ft.Icons.CIRCLE, size=12, color=ft.Colors.BLUE_300), ft.Text("Relevantes", size=13, expand=True), ft.Text("18", size=13), ft.Icon(ft.Icons.CHEVRON_RIGHT, size=14, color=ft.Colors.WHITE_38)]),
            ft.Row([ft.Icon(ft.Icons.CIRCLE, size=12, color=ft.Colors.PURPLE_300), ft.Text("Pendentes", size=13, expand=True), ft.Text("8", size=13)]),
        ],
        spacing=8,
        expand=True
    )

    card_requisitos = ft.Column(
        [
            ft.Row([ft.Text("Requisitos mais exigidos", weight=ft.FontWeight.BOLD, size=16), ft.Text("Ver todos →", size=10, color=ft.Colors.WHITE_54)], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(color=ft.Colors.with_opacity(0.05, ft.Colors.WHITE), height=10),
            ft.Row([ft.Text("Java", size=12, width=80), ft.ProgressBar(value=0.8, color=ft.Colors.PURPLE_300, expand=True, height=6), ft.Text("18", size=12, width=20)], expand=True),
            ft.Row([ft.Text("SQL", size=12, width=80), ft.ProgressBar(value=0.6, color=ft.Colors.PURPLE_300, expand=True, height=6), ft.Text("15", size=12, width=20)], expand=True),
            ft.Row([ft.Text("Spring Boot", size=12, width=80), ft.ProgressBar(value=0.5, color=ft.Colors.PURPLE_300, expand=True, height=6), ft.Text("12", size=12, width=20)], expand=True),
        ],
        spacing=8,
        expand=True
    )

    cards = [
        make_draggable_resizable_card(card_progresso, top=15, left=15, width=390, height=195),
        make_draggable_resizable_card(card_mercado, top=15, left=420, width=330, height=195),
        make_draggable_resizable_card(card_carreiras, top=225, left=15, width=300, height=210),
        make_draggable_resizable_card(card_requisitos, top=225, left=330, width=420, height=210),
    ]
    
    dashboard_area.controls.extend(cards)
    return dashboard_area