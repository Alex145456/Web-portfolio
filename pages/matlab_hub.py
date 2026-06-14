import flet as ft

from components.section import info_card, page_header


COURSES = [
    {
        "name": "MATLAB Onramp",
        "file": "certificates/Matlab Onramp.png",
        "status": "Uploaded certificate",
    },
    {
        "name": "Calculations with Vectors and Matrices",
        "file": "certificates/Calculation with Vectors and Matrices.png",
        "status": "Uploaded certificate",
    },
    {
        "name": "Explore Data with MATLAB Plots",
        "file": "certificates/Explore Data with Matlab Plots.png",
        "status": "Uploaded certificate",
    },
    {
        "name": "MATLAB Desktop Tools and Troubleshooting Scripts",
        "file": "certificates/Matlab Desktop Tools and Troubleshooting Scripts.png",
        "status": "Uploaded certificate",
    },
    {
        "name": "Machine Learning Onramp",
        "file": "certificates/Machine Learning Onramp.png",
        "status": "Uploaded certificate",
    },
]


def certificate_card(index: int, course: dict, page: ft.Page) -> ft.Container:
    uploaded = course["file"] is not None
    cert_route = f"/certificate/{index - 1}"
    return ft.Container(
        padding=ft.Padding.all(16),
        border_radius=8,
        bgcolor="#0d1d31",
        border=ft.Border.all(1, "#173554"),
        content=ft.Column(
            controls=[
                ft.Container(
                    height=110,
                    alignment=ft.Alignment(0, 0),
                    border_radius=8,
                    bgcolor="#08182b",
                    border=ft.Border.all(1, "#1d5f9f" if uploaded else "#34465d"),
                    content=ft.Column(
                        controls=[
                            ft.Icon(ft.Icons.MILITARY_TECH, color="#f0bf63" if uploaded else "#6c7d94", size=38),
                            ft.Text("Certificate Uploaded" if uploaded else "Certificate Slot", size=12, color="#b6c6dc"),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=6,
                    ),
                ),
                ft.Text(f"{index}. {course['name']}", size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(
                    course["status"],
                    size=12,
                    color="#9fb1c8",
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "View in app" if uploaded else "Waiting for file",
                            icon=ft.Icons.VISIBILITY if uploaded else ft.Icons.HOURGLASS_EMPTY,
                            disabled=not uploaded,
                            on_click=lambda _, r=cert_route: page.go(r),
                            style=ft.ButtonStyle(
                                color="#06101d" if uploaded else "#6c7d94",
                                bgcolor="#f0bf63" if uploaded else "#132338",
                                shape=ft.RoundedRectangleBorder(radius=8),
                            ),
                        ),
                        ft.IconButton(
                            icon=ft.Icons.OPEN_IN_NEW,
                            icon_color="#61a5ff" if uploaded else "#34465d",
                            tooltip="Open PDF in browser",
                            url=course["file"] if uploaded else None,
                            disabled=not uploaded,
                        ),
                    ],
                    spacing=8,
                    wrap=True,
                ),
                ft.TextButton(
                    "Related blog: mass balance",
                    icon=ft.Icons.ARTICLE,
                    on_click=lambda _: page.go("/blog"),
                    style=ft.ButtonStyle(
                        color="#9fb1c8",
                    ),
                ),
            ],
            spacing=12,
        ),
    )


def build_matlab_page(page: ft.Page) -> ft.Control:
    return ft.Column(
        controls=[
            page_header(
                "MATLAB Achievement Hub",
                "Proof area for eight MathWorks Learning Center course completions.",
                ft.Icons.SCHOOL,
            ),
            info_card(
                "Certificate assets",
                "Four supplied certificate PDFs are now placed in assets/certificates and linked by course name.",
                ft.Icons.FOLDER_OPEN,
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        "Read Technical Blog",
                        icon=ft.Icons.ARTICLE,
                        on_click=lambda _: page.go("/blog"),
                        style=ft.ButtonStyle(
                            color="#06101d",
                            bgcolor="#f0bf63",
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                    ),
                    ft.OutlinedButton(
                        "See GitHub Evidence",
                        icon=ft.Icons.CODE,
                        on_click=lambda _: page.go("/github"),
                        style=ft.ButtonStyle(
                            color="#b6c6dc",
                            side=ft.BorderSide(1, "#2a4f7d"),
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                    ),
                ],
                spacing=12,
                wrap=True,
            ),
            ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        col={"xs": 12, "sm": 6, "lg": 3},
                        content=certificate_card(index, course, page),
                    )
                    for index, course in enumerate(COURSES, start=1)
                ],
                spacing=14,
                run_spacing=14,
            ),
        ],
        spacing=18,
        scroll=ft.ScrollMode.AUTO,
    )


def build_certificate_page(page: ft.Page, route: str) -> ft.Control:
    try:
        index = int(route.strip("/").split("/")[-1])
    except ValueError:
        index = 0

    if index < 0 or index >= len(COURSES) or COURSES[index]["file"] is None:
        return ft.Column(
            controls=[
                page_header("Certificate Viewer", "The selected certificate could not be found.", ft.Icons.WARNING),
                ft.ElevatedButton("Back to MATLAB Hub", icon=ft.Icons.ARROW_BACK, on_click=lambda _: page.go("/matlab")),
            ],
            spacing=18,
        )

    course = COURSES[index]
    file_url = course["file"]
    return ft.Column(
        controls=[
            page_header(course["name"], "Certificate preview inside the Flet portfolio.", ft.Icons.MILITARY_TECH),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        "Back to MATLAB Hub",
                        icon=ft.Icons.ARROW_BACK,
                        on_click=lambda _: page.go("/matlab"),
                        style=ft.ButtonStyle(
                            color="#06101d",
                            bgcolor="#f0bf63",
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                    ),
                    ft.OutlinedButton(
                        "Open asset",
                        icon=ft.Icons.OPEN_IN_NEW,
                        url=file_url,
                        style=ft.ButtonStyle(
                            color="#b6c6dc",
                            side=ft.BorderSide(1, "#2a4f7d"),
                            shape=ft.RoundedRectangleBorder(radius=8),
                        ),
                    ),
                ],
                spacing=12,
                wrap=True,
            ),
            # Use embedded WebView when available; otherwise show a browser fallback
            ft.Container(
                height=620,
                border_radius=8,
                bgcolor="#0d1d31",
                border=ft.Border.all(1, "#173554"),
                padding=ft.Padding.all(8),
                content=(
                    (
                        ft.Image(src=file_url, fit="contain", expand=True)
                        if any(file_url.lower().endswith(ext) for ext in (".png", ".jpg", ".jpeg", ".webp"))
                        else (
                            ft.WebView(url=file_url, expand=True, enable_javascript=True, bgcolor="#0d1d31")
                            if hasattr(ft, "WebView")
                            else ft.Column(
                                controls=[
                                    ft.Text(
                                        "Embedded preview is not available in this environment.",
                                        color="#b6c6dc",
                                    ),
                                    ft.Text("Click the button to open the asset in your browser.", color="#9fb1c8"),
                                    ft.Row(
                                        controls=[
                                            ft.ElevatedButton(
                                                "Open in browser",
                                                icon=ft.Icons.OPEN_IN_NEW,
                                                on_click=lambda _: page.launch_url(file_url),
                                                style=ft.ButtonStyle(
                                                    color="#06101d",
                                                    bgcolor="#f0bf63",
                                                    shape=ft.RoundedRectangleBorder(radius=8),
                                                ),
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=12,
                            )
                        )
                    )
                ),
            ),
        ],
        spacing=18,
    )
