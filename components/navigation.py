import flet as ft


ROUTES = [
    ("home", "Home", ft.Icons.HOME),
    ("timeline", "Timeline", ft.Icons.TIMELINE),
    ("matlab", "MATLAB", ft.Icons.SCHOOL),
    ("blog", "Blog", ft.Icons.ARTICLE),
    ("github", "GitHub", ft.Icons.CODE),
]


def build_nav(page: ft.Page, selected_route: str) -> ft.Container:
    def go(route: str):
        page.go(f"/{route}")

    nav_items = []
    for route, label, icon in ROUTES:
        selected = route == selected_route
        nav_items.append(
            ft.Container(
                padding=ft.Padding.symmetric(horizontal=16, vertical=14),
                border_radius=12,
                bgcolor="#0f172a" if selected else "transparent",
                border=ft.Border.all(1, "#1f2937" if selected else "transparent"),
                content=ft.TextButton(
                    label,
                    icon=icon,
                    style=ft.ButtonStyle(
                        color="#ffffff" if selected else "#94a3b8",
                        padding=ft.Padding.all(0),
                    ),
                    on_click=lambda _, r=route: go(r),
                ),
            )
        )

    return ft.Container(
        width=280,
        padding=ft.Padding.all(20),
        bgcolor="#0b1f3a",

        border=ft.Border.only(right=ft.border.BorderSide(1, "#172a45")),
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            width=46,
                            height=46,
                            alignment=ft.Alignment(0, 0),
                            border_radius=12,
                            bgcolor="#0ea5e9",
                            content=ft.Text("AA", color="#ffffff", weight=ft.FontWeight.BOLD, size=16),
                        ),
                        ft.Column(
                            controls=[
                                ft.Text("Angula Absalom", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                ft.Text("UNAM Mechanical Engineering", size=12, color="#94a3b8"),
                            ],
                            spacing=4,
                            expand=True,
                        ),
                    ],
                    spacing=14,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Container(height=36),
                ft.Column(
                    controls=nav_items,
                    spacing=8,
                ),
                ft.Container(expand=True),
                ft.Text("© 2026 Portfolio", size=11, color="#475569"),
            ],
            spacing=0,
            expand=True,
        ),
    )
