import flet as ft
from src.components.glass_container import create_glass_card

def build_dashboard() -> ft.Column:
    # 1. Boas-vindas
    welcome_section = ft.Row(
        [
            ft.Text("🌟", size=40),
            ft.Column(
                [
                    ft.Text("Bem-vindo de volta, viajante.", size=28, weight=ft.FontWeight.BOLD),
                    ft.Text("Mais um passo em direção aos seus sonhos. ✨", size=16, color=ft.Colors.WHITE_70),
                ],
                spacing=5,
            )
        ],
    )

    # 2. Cartões de Progresso e Números
    row_top_cards = ft.Row(
        [
            create_glass_card(
                content=ft.Column(
                    [
                        ft.Row([ft.Text("Seu progresso 📈", weight=ft.FontWeight.BOLD), ft.Icon(ft.Icons.MORE_HORIZ)]),
                        ft.Row(
                            [
                                ft.ProgressRing(value=0.72, width=80, height=80, stroke_width=8, color=ft.Colors.PURPLE_300),
                                ft.Column(
                                    [
                                        ft.Checkbox(label="Revisar requisitos", value=True),
                                        ft.Checkbox(label="Concluir Spring Boot", value=False),
                                    ],
                                    spacing=5,
                                ),
                            ],
                            spacing=20,
                        )
                    ]
                ),
                expand=True,
                height=180,
            ),
            create_glass_card(
                content=ft.Column(
                    [
                        ft.Row([ft.Text("O mercado em números 📊", weight=ft.FontWeight.BOLD)]),
                        ft.Row(
                            [
                                ft.Column([ft.Text("1.2k", size=30, weight=ft.FontWeight.BOLD), ft.Text("vagas analisadas", size=12, color=ft.Colors.WHITE_54)]),
                                ft.Column([ft.Text("37", size=30, weight=ft.FontWeight.BOLD), ft.Text("novos requisitos", size=12, color=ft.Colors.WHITE_54)]),
                            ],
                            spacing=40,
                        ),
                    ]
                ),
                expand=True,
                height=180,
            ),
        ],
        spacing=20,
    )

    # 3. Carreiras e Requisitos
    row_middle_cards = ft.Row(
        [
            create_glass_card(
                content=ft.Column(
                    [
                        ft.Row([ft.Text("Suas carreiras 💼", weight=ft.FontWeight.BOLD), ft.Text("Ver todos", size=12, color=ft.Colors.PURPLE_300)]),
                        ft.ListTile(leading=ft.Text("⭐"), title=ft.Text("Favoritos"), trailing=ft.Text("12")),
                        ft.ListTile(leading=ft.Text("🔵"), title=ft.Text("Relevantes"), trailing=ft.Text("18")),
                    ],
                    spacing=0,
                ),
                expand=True,
            ),
            create_glass_card(
                content=ft.Column(
                    [
                        ft.Row([ft.Text("Requisitos exigidos 🎯", weight=ft.FontWeight.BOLD), ft.Text("Ver todos", size=12, color=ft.Colors.PURPLE_300)]),
                        ft.Text("Java", size=12),
                        ft.ProgressBar(value=0.8, color=ft.Colors.PURPLE_300, bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.WHITE)),
                        ft.Text("SQL", size=12),
                        ft.ProgressBar(value=0.6, color=ft.Colors.PURPLE_300, bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.WHITE)),
                    ],
                    spacing=10,
                ),
                expand=True,
            ),
        ],
        spacing=20,
    )

    # 4. Cursos Recomendados
    row_bottom_cards = ft.Row(
        [
            create_glass_card(
                content=ft.Column(
                    [
                        ft.Row([ft.Text("Cursos recomendados 🎓", weight=ft.FontWeight.BOLD), ft.Text("Ver todos", size=12, color=ft.Colors.PURPLE_300)]),
                        ft.Row(
                            [
                                ft.Container(
                                    content=ft.Column([ft.Text("☕ Java Completo", size=12), ft.Text("Udemy", size=10, color=ft.Colors.WHITE_54)]),
                                    bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                                    padding=10, border_radius=10, expand=True
                                ),
                                ft.Container(
                                    content=ft.Column([ft.Text("🐳 Docker Essencial", size=12), ft.Text("Coursera", size=10, color=ft.Colors.WHITE_54)]),
                                    bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                                    padding=10, border_radius=10, expand=True
                                ),
                            ],
                            spacing=10,
                        )
                    ]
                ),
                expand=True,
            )
        ]
    )

    return ft.Column(
        [welcome_section, row_top_cards, row_middle_cards, row_bottom_cards],
        spacing=20,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )