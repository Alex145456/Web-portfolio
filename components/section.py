import flet as ft


def page_header(title: str, subtitle: str, icon: str) -> ft.Container:
    return ft.Container(
        padding=ft.Padding.only(bottom=18),
        content=ft.Row(
            controls=[
                ft.Container(
                    width=52,
                    height=52,
                    alignment=ft.Alignment(0, 0),
                    border_radius=8,
                    bgcolor="#10243b",
                    border=ft.Border.all(1, "#1d5f9f"),
                    content=ft.Icon(icon, color="#61a5ff", size=28),
                ),
                ft.Column(
                    controls=[
                        ft.Text(title, size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(subtitle, size=14, color="#9fb1c8"),
                    ],
                    spacing=4,
                    expand=True,
                ),
            ],
            spacing=16,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )


def info_card(title: str, body: str, icon: str = ft.Icons.INFO_OUTLINE) -> ft.Container:
    return ft.Container(
        padding=ft.Padding.all(18),
        border_radius=8,
        bgcolor="#0d1d31",
        border=ft.Border.all(1, "#173554"),
        content=ft.Row(
            controls=[
                ft.Icon(icon, color="#61a5ff"),
                ft.Column(
                    controls=[
                        ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(body, size=13, color="#b6c6dc"),
                    ],
                    spacing=6,
                    expand=True,
                ),
            ],
            spacing=12,
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
    )


def formula_box(expression: str, explanation: str) -> ft.Container:
    return ft.Container(
        padding=ft.Padding.all(16),
        border_radius=8,
        bgcolor="#08182b",
        border=ft.Border.all(1, "#1d5f9f"),
        content=ft.Column(
            controls=[
                ft.Text(expression, size=20, weight=ft.FontWeight.BOLD, color="#8ec5ff"),
                ft.Text(explanation, size=13, color="#b6c6dc"),
            ],
            spacing=8,
        ),
    )
