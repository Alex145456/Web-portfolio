import flet as ft

from components.navigation import build_nav
from pages.blog import build_blog_page
from pages.github_evidence import build_github_page
from pages.home import build_home_page
from pages.matlab_hub import build_certificate_page, build_matlab_page
from pages.timeline import build_timeline_page


PAGE_BUILDERS = {
    "home": build_home_page,
    "timeline": build_timeline_page,
    "matlab": build_matlab_page,
    "blog": build_blog_page,
    "github": build_github_page,
}


def route_to_key(route: str) -> str:
    if route.startswith("/certificate/"):
        return "matlab"
    key = route.strip("/") or "home"
    return key if key in PAGE_BUILDERS else "home"


def main(page: ft.Page) -> None:
    page.title = "Engineering Portfolio"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#0b1f3a"
    page.padding = 0
    page.window_min_width = 1000
    page.window_min_height = 720

    def render(route: str) -> None:
        selected = route_to_key(route)
        print(f"render(): route={route!r} -> selected={selected!r}")
        content = build_certificate_page(page, route) if route.startswith("/certificate/") else PAGE_BUILDERS[selected](page)
        page.controls.clear()
        page.add(
            ft.Row(
                controls=[
                    build_nav(page, selected),
                    ft.Container(
                        expand=True,
                        padding=ft.Padding.symmetric(horizontal=50, vertical=40),
                        bgcolor="#0b1f3a",
                        content=content,
                    ),
                ],
                spacing=0,
                expand=True,
            )
        )
        page.update()

    def _on_route_change(event):
        print(f"on_route_change: event.route={event.route!r}")
        render(event.route)

    page.on_route_change = _on_route_change
    render(page.route)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
