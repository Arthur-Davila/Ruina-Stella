import flet as ft
from src.components.glass_container import create_glass_card

def build_jarvis_panel() -> ft.Container:
    return create_glass_card(
        content=ft.Column(
            [
                # Cabeçalho
                ft.Row(
                    [
                        ft.Row([ft.Icon(ft.Icons.AUTO_AWESOME, color=ft.Colors.PURPLE_300, size=20), ft.Text("Jarvis", weight=ft.FontWeight.BOLD, size=18)]),
                        ft.Row([ft.Container(width=8, height=8, bgcolor=ft.Colors.GREEN, border_radius=4), ft.Text("Online", size=12, color=ft.Colors.GREEN)]),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE)),
                
                # Chat
                ft.Column(
                    [
                        ft.Container(
                            content=ft.Text("O que você acha dessa vaga?", size=13),
                            bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.PURPLE_300),
                            padding=12,
                            border_radius=ft.BorderRadius.only(
                                top_left=10, top_right=10, bottom_left=10
                            ),
                            alignment=ft.Alignment(-1, 0),
                        ),
                        ft.Container(
                            content=ft.Column([
                                ft.Text("Essa vaga parece uma ótima oportunidade para você!", size=13),
                                ft.Text("Você atende 75% dos requisitos.\n• Spring Boot\n• Docker\n• APIs REST", size=12, color=ft.Colors.WHITE_70)
                            ]),
                            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                            padding=12,
                            border_radius=ft.BorderRadius.only(
                                top_left=10, top_right=10, bottom_right=10
                            ),
                        ),
                    ],
                    spacing=15,
                    scroll=ft.ScrollMode.AUTO,
                    expand=True,
                ),
                
                # Input
                ft.TextField(
                    hint_text="Pergunte algo...",
                    border_radius=20,
                    filled=True,
                    bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                    suffix_icon=ft.Icons.SEND,
                )
            ],
            spacing=15,
        ),
        width=320,
    )