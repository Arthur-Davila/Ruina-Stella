import flet as ft
from src.config import GLASS_BG_COLOR, GLASS_BORDER_COLOR


def create_glass_card(
    content: ft.Control,
    padding: int = 20,
    *,
    width: int | float | None = None,
    height: int | float | None = None,
    expand: bool | int | None = None,
) -> ft.Container:
    """Cria um contêiner reutilizável com transparência e desfoque (efeito vidro)."""
    return ft.Container(
        content=content,
        padding=padding,
        width=width,
        height=height,
        expand=expand,
        border_radius=16,
        bgcolor=GLASS_BG_COLOR,
        border=ft.Border.all(1, GLASS_BORDER_COLOR),
        blur=ft.Blur(15, 15, ft.BlurTileMode.CLAMP),
    )