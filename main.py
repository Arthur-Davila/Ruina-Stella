import flet as ft
from src.components.sidebar import build_sidebar
from src.components.top_bar import build_top_bar
from src.components.dashboard_content import build_dashboard
from src.components.jarvis_panel import build_jarvis_panel
from src.config import OVERLAY_COLOR

def main(page: ft.Page):
    page.title = "Ruina Stella - Teste"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    page.window.maximized = True

    # Fundo
    bg_image = ft.Image(src="background8.jpg", fit=ft.BoxFit.COVER, expand=True)

    # Componentes
    sidebar = build_sidebar()
    top_bar = build_top_bar()
    dashboard = build_dashboard(page)
    jarvis = build_jarvis_panel()

    # Área central (TopBar fixo em cima, Dashboard solto abaixo)
    center_area = ft.Container(
        content=ft.Column([
            top_bar,
            ft.Container(content=dashboard, expand=True) # Onde os cards flutuam
        ], expand=True),
        padding=30,
        expand=True,
    )

    # Layout Principal
    main_ui = ft.Container(
        content=ft.Row(
            [
                ft.Container(sidebar, width=240),
                center_area,
                ft.Container(jarvis, padding=ft.Padding.only(top=30, right=30, bottom=30)),
            ],
            expand=True,
            spacing=0,
        ),
        padding=16,
        expand=True,
    )

    # Stack Principal
    layout = ft.Stack(
        controls=[
            ft.Container(content=bg_image, expand=True),
            ft.Container(bgcolor=OVERLAY_COLOR, expand=True),
            main_ui,
        ],
        fit=ft.StackFit.EXPAND,
        expand=True,
    )

    page.add(layout)

if __name__ == "__main__":
    ft.run(main, assets_dir="assets")