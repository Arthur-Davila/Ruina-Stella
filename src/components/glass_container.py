import flet as ft

def create_glass_card(content, width=None, height=None, padding=20, expand=False):
    return ft.Container(
        content=content,
        width=width,
        height=height,
        padding=padding,
        expand=expand,
        # Gradiente escuro e transparente (fosco)
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[
                ft.Colors.with_opacity(0.6, "#1e1e2e"), # Topo esquerdo mais claro
                ft.Colors.with_opacity(0.2, "#11111b")  # Fundo direito quase preto
            ]
        ),
        border=ft.border.all(1, ft.Colors.with_opacity(0.05, ft.Colors.WHITE)), # Borda quase invisível
        border_radius=16,
        # Sombra para dar profundidade (dá o aspecto fosco sem precisar de blur pesado)
        shadow=ft.BoxShadow(
            blur_radius=20,
            color=ft.Colors.with_opacity(0.4, ft.Colors.BLACK),
            offset=ft.Offset(0, 8),
        )
    )