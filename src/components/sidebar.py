import flet as ft
from src.components.glass_container import create_glass_card


def build_sidebar() -> ft.Container:
    nav_items = [
        ("🏠", "Dashboard"),
        ("💼", "Carreiras"),
        ("🎓", "Cursos"),
        ("🏆", "Concursos"),
        ("🏛️", "Faculdade"),
        ("💻", "Projetos"),
    ]

    sidebar_controls = [
        ft.Row(
            [
                ft.Text("🪐", size=28),
                ft.Column(
                    [
                        ft.Text(
                            "Ruina Stella", size=20, weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            "Organize. Aprenda. Conquiste.",
                            size=10,
                            color=ft.Colors.WHITE_54,
                        ),
                    ],
                    spacing=0,
                ),
            ]
        ),
        ft.Divider(color=ft.Colors.WHITE_12, height=20),  # WHITE12 -> WHITE_12
    ]

    for icon, label in nav_items:
        sidebar_controls.append(
            ft.TextButton(
                content=ft.Row([ft.Text(icon), ft.Text(label, color=ft.Colors.WHITE)]),
                style=ft.ButtonStyle(padding=12),
            )
        )

    sidebar_controls.extend(
        [
            ft.Container(expand=True),
            ft.Text(
                '"Talvez o universo esteja conspirando a seu favor."\n— Mario Galaxy',
                size=11,
                color=ft.Colors.WHITE_38,  # WHITE38 -> WHITE_38
                italic=True,
            ),
        ]
    )

    return create_glass_card(ft.Column(sidebar_controls, expand=True))