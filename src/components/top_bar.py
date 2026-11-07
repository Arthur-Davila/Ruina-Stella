import flet as ft

def build_top_bar() -> ft.Row:
    return ft.Row(
        [
            # Barra de Pesquisa
            ft.Container(
                content=ft.TextField(
                    hint_text="Pesquisar vagas, cursos, requisitos...",
                    prefix_icon=ft.Icons.SEARCH,
                    border=ft.InputBorder.NONE,
                    filled=True,
                    fill_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                    expand=True,
                    height=45,
                ),
                expand=True,
                padding=ft.padding.Padding(right=50),
            ),
            # Ícones da direita (Notificação, Config, Perfil)
            ft.Row(
                [
                    ft.IconButton(ft.Icons.NOTIFICATIONS_OUTLINED, icon_color=ft.Colors.WHITE),
                    ft.IconButton(ft.Icons.SETTINGS_OUTLINED, icon_color=ft.Colors.WHITE),
                    ft.CircleAvatar(
                        foreground_image_src="https://i.pravatar.cc/150?img=11", # Avatar de exemplo
                        radius=20,
                    ),
                ],
                spacing=10,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )