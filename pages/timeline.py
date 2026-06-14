import flet as ft

from components.section import info_card, page_header


WEEKLY_LOGS = [
    {
        "week": "Week 1",
        "title": "Requirements and module scoping",
        "contribution": "Mapped project requirements to Metallurgical Engineering workflows. Defined data fields for feed material, product streams, waste streams, recovery, and processing assumptions.",
        "evidence": "Created initial task board and drafted the shared architecture outline.",
    },
    {
        "week": "Week 2",
        "title": "Cost model prototype",
        "contribution": "Built the first metallurgical calculation logic for mass balance, recovery percentage, and process-cost assumptions.",
        "evidence": "Committed a working calculation prototype and documented test cases.",
    },
    {
        "week": "Week 3",
        "title": "Engineering validation",
        "contribution": "Compared calculated outputs against hand calculations to confirm formula correctness and identify edge cases.",
        "evidence": "Added validation notes and sample calculation screenshots.",
    },
    {
        "week": "Week 4",
        "title": "Interface and reporting",
        "contribution": "Improved navigation, added result summaries, and prepared outputs suitable for technical review.",
        "evidence": "Opened pull request for UI polish and report export improvements.",
    },
]


def timeline_item(log: dict) -> ft.Container:
    return ft.Container(
        padding=ft.Padding.all(18),
        border_radius=8,
        bgcolor="#0d1d31",
        border=ft.Border.all(1, "#173554"),
        content=ft.Row(
            controls=[
                ft.Container(
                    width=86,
                    alignment=ft.Alignment(0, 0),
                    padding=ft.Padding.symmetric(vertical=10),
                    border_radius=8,
                    bgcolor="#1d6fff",
                    content=ft.Text(log["week"], color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                ),
                ft.Column(
                    controls=[
                        ft.Text(log["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(log["contribution"], size=13, color="#b6c6dc"),
                        ft.Container(
                            padding=ft.Padding.all(10),
                            border_radius=8,
                            bgcolor="#08182b",
                            border=ft.Border.all(1, "#173554"),
                            content=ft.Text(f"Evidence: {log['evidence']}", size=12, color="#9fb1c8"),
                        ),
                    ],
                    spacing=10,
                    expand=True,
                ),
            ],
            spacing=16,
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
    )


def build_timeline_page(page: ft.Page) -> ft.Control:
    return ft.Column(
        controls=[
            page_header(
                "Project Timeline",
                "Weekly contribution log for the Metallurgical Engineering group project.",
                ft.Icons.TIMELINE,
            ),
            info_card(
                "How to use this page",
                "Replace each sample week with your exact tasks, dates, commits, screenshots, and peer-review evidence.",
                ft.Icons.EDIT_NOTE,
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        "View GitHub Evidence",
                        icon=ft.Icons.CODE,
                        on_click=lambda _: page.go("/github"),
                        style=ft.ButtonStyle(color="#06101d", bgcolor="#f0bf63", shape=ft.RoundedRectangleBorder(radius=8)),
                    ),
                    ft.OutlinedButton(
                        "Open MATLAB Hub",
                        icon=ft.Icons.SCHOOL,
                        on_click=lambda _: page.go("/matlab"),
                        style=ft.ButtonStyle(color="#b6c6dc", side=ft.BorderSide(1, "#2a4f7d"), shape=ft.RoundedRectangleBorder(radius=8)),
                    ),
                ],
                spacing=12,
                wrap=True,
            ),
            ft.Column(controls=[timeline_item(log) for log in WEEKLY_LOGS], spacing=14),
        ],
        spacing=18,
        scroll=ft.ScrollMode.AUTO,
    )
