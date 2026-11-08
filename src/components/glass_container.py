import flet as ft

def create_glass_card(content, width=None, height=None, padding=20, expand=False):
    return ft.Container(
        content=content,
        width=width,
        height=height,
        padding=padding,
        expand=expand,
        gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_LEFT,
            end=ft.Alignment.BOTTOM_RIGHT,
            colors=[
                ft.Colors.with_opacity(0.6, "#1e1e2e"),
                ft.Colors.with_opacity(0.2, "#11111b")
            ]
        ),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.05, ft.Colors.WHITE)),
        border_radius=16,
        shadow=ft.BoxShadow(
            blur_radius=20,
            color=ft.Colors.with_opacity(0.4, ft.Colors.BLACK),
            offset=ft.Offset(0, 8),
        )
    )