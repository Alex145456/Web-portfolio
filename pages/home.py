import flet as ft


def build_home_page(page: ft.Page) -> ft.Control:
    # --- Small helpers to keep style consistent ---
    def card_style():
        return dict(
            border_radius=24,
            bgcolor="#0f172a",
            border=ft.Border.all(1, "#172a45"),
        )

    def primary_button(label: str, icon: str, bgcolor: str, on_click):
        return ft.ElevatedButton(
            label,
            icon=icon,
            style=ft.ButtonStyle(
                color="#ffffff",
                bgcolor=bgcolor,
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=ft.Padding.symmetric(horizontal=22, vertical=14),
            ),
            on_click=on_click,
        )

    def secondary_button(label: str, icon: str, on_click):
        return ft.OutlinedButton(
            label,
            icon=icon,
            style=ft.ButtonStyle(
                color="#94a3b8",
                side=ft.BorderSide(1, "#334155"),
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=ft.Padding.symmetric(horizontal=22, vertical=14),
            ),
            on_click=on_click,
        )

    def focus_item(icon, icon_color: str, title: str, subtitle: str) -> ft.Container:
        return ft.Container(
            padding=ft.Padding.all(18),
            border_radius=16,
            bgcolor="#111827",
            border=ft.Border.all(1, "#1f2a3d"),
            content=ft.Row(
                controls=[
                    ft.Container(
                        width=42,
                        height=42,
                        alignment=ft.Alignment(0, 0),
                        border_radius=12,
                        bgcolor="#0b1220",
                        border=ft.Border.all(1, "#172a45"),
                        content=ft.Icon(icon, color=icon_color, size=20),
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text(subtitle, size=12, color="#94a3b8"),
                        ],
                        spacing=4,
                        expand=True,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    # --- Linear / professional hero stack ---
    return ft.Column(
        controls=[
            # HERO (single column)
            ft.Container(
                padding=ft.Padding.all(26),
                **card_style(),
                content=ft.Column(
                    controls=[
                        ft.Container(
                            padding=ft.Padding.symmetric(horizontal=14, vertical=10),
                            border_radius=12,
                            bgcolor="#10243b",
                            content=ft.Text(
                                "Portfolio",
                                size=12,
                                weight=ft.FontWeight.BOLD,
                                color="#38bdf8",
                            ),
                        ),
                        ft.Container(height=18),
                        ft.Text("Alexander Absalom", size=44, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Container(height=6),
                        ft.Text(
                            "Second-Year Mechanical Engineering Student | UNAM",
                            size=16,
                            color="#94a3b8",
                            weight=ft.FontWeight.W_500,
                        ),
                        ft.Container(height=10),
                        ft.Text(
                            "AlexanderAbsalom145@gmail.com",
                            size=13,
                            color="#38bdf8",
                            selectable=True,
                        ),
                        ft.Container(height=18),
                        ft.Text(
                            "I’m a second-year Mechanical Engineering student with a strong passion for technology, innovation, and problem-solving. I’m particularly interested in programming, electronics, and system design, and I enjoy building practical projects—web applications and physics-based simulations—using Python.",
                            size=14,
                            color="#cbd5e1",
                        ),
                        ft.Text(
                            "Through academic work and personal projects, I develop skills in software development, engineering design, and technical problem-solving with the goal of becoming a well-rounded engineer in modern technology.",
                            size=14,
                            color="#cbd5e1",
                        ),
                        ft.Container(height=22),
                        ft.Row(
                            controls=[
                                primary_button(
                                    "Email Me",
                                    ft.Icons.EMAIL,
                                    "#ef4444",
                                    lambda _: page.launch_url("mailto:AlexanderAbsalom145@gmail.com"),
                                ),
                                primary_button(
                                    "GitHub",
                                    ft.Icons.LINK,
                                    "#0ea5e9",
                                    lambda _: page.launch_url("https://github.com/ceubilly"),
                                ),
                                secondary_button(
                                    "About Me",
                                    ft.Icons.PERSON,
                                    lambda _: page.go("/blog"),
                                ),
                            ],
                            spacing=12,
                            wrap=True,
                        ),
                        ft.Container(height=6),
                    ],
                    spacing=0,
                ),
            ),

            # FOCUS BOARD (linear list)
            ft.Container(
                padding=ft.Padding.all(26),
                border_radius=24,
                bgcolor="#0f172a",
                border=ft.Border.all(1, "#172a45"),
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.SETTINGS, color="#38bdf8", size=28),
                                ft.Text(
                                    "Engineering Focus",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                            ],
                            spacing=12,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ft.Container(height=10),
                        ft.Text(
                            "Programming, electronics, system design, simulations, data, and documentation—presented with a clean Python interface and UNAM identity.",
                            size=13,
                            color="#94a3b8",
                        ),
                        ft.Container(height=20),
                        ft.Column(
                            controls=[
                                focus_item(
                                    ft.Icons.HANDYMAN,
                                    "#f87171",
                                    "Machine Design",
                                    "shafts, gears, fasteners",
                                ),
                                focus_item(
                                    ft.Icons.LOCAL_FIRE_DEPARTMENT,
                                    "#fbbf24",
                                    "Thermodynamics",
                                    "energy, heat, efficiency",
                                ),
                                focus_item(
                                    ft.Icons.SCIENCE,
                                    "#34d399",
                                    "Materials",
                                    "stress, strain, failure",
                                ),
                                focus_item(
                                    ft.Icons.TRENDING_UP,
                                    "#38bdf8",
                                    "Simulation",
                                    "model, plot, improve",
                                ),
                            ],
                            spacing=12,
                        ),
                    ],
                    spacing=0,
                ),
            ),

            # Video (hosted URL)
            # NOTE: Flet v0.85.3 in this project does not include ft.Video.
            # So we display a professional video placeholder card and allow opening the MP4.
            ft.Container(
                padding=ft.Padding.all(26),
                border_radius=24,
                bgcolor="#0f172a",
                border=ft.Border.all(1, "#172a45"),
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Icon(ft.Icons.VIDEOCAM, color="#38bdf8", size=28),
                                ft.Text(
                                    "Featured Video",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                            ],
                            spacing=12,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ft.Container(height=14),
                        ft.Container(
                            height=220,
                            border_radius=14,
                            bgcolor="#08182b",
                            border=ft.Border.all(1, "#173554"),
                            content=ft.Column(
                                controls=[
                                    ft.Icon(ft.Icons.PLAY_CIRCLE, size=54, color="#61a5ff"),
                                    ft.Text("Video preview unavailable in this Flet version", size=13, color="#9fb1c8"),
                                    ft.Text("Click below to play the MP4", size=11, color="#94a3b8"),
                                    ft.Container(height=12),
                                    ft.ElevatedButton(
                                        "Open Video",
                                        icon=ft.Icons.OPEN_IN_NEW,
                                        style=ft.ButtonStyle(
                                            color="#ffffff",
                                            bgcolor="#0ea5e9",
                                            shape=ft.RoundedRectangleBorder(radius=10),
                                        ),
                                        on_click=lambda _: page.launch_url("https://files.catbox.moe/mcrrfa.mp4"),
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=6,
                            ),
                        ),
                    ],
                    spacing=0,
                ),
            ),


            # Lower section cards (kept, but aligned/standardized)
            ft.Container(height=10),
            ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        col={"xs": 12, "md": 4},
                        padding=ft.Padding.all(22),
                        border_radius=20,
                        bgcolor="#0f172a",
                        border=ft.Border.all(1, "#172a45"),
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.SHOW_CHART, color="#facc15", size=22),
                                        ft.Text("Timeline", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ],
                                    spacing=10,
                                ),
                                ft.Text("Week 1 to Week 6 contribution log.", size=13, color="#94a3b8"),
                                ft.Container(height=16),
                                ft.ElevatedButton(
                                    "Open Timeline",
                                    icon=ft.Icons.OPEN_IN_NEW,
                                    style=ft.ButtonStyle(
                                        color="#ffffff",
                                        bgcolor="#0ea5e9",
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    on_click=lambda _: page.go("/timeline"),
                                ),
                            ],
                            spacing=16,
                        ),
                    ),
                    ft.Container(
                        col={"xs": 12, "md": 4},
                        padding=ft.Padding.all(22),
                        border_radius=20,
                        bgcolor="#0f172a",
                        border=ft.Border.all(1, "#172a45"),
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.PICTURE_AS_PDF, color="#ef4444", size=22),
                                        ft.Text(
                                            "MATLAB Certificates",
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                    ],
                                    spacing=10,
                                ),
                                ft.Text(
                                    "Uploaded certificates open from the certificate cards.",
                                    size=13,
                                    color="#94a3b8",
                                ),
                                ft.Container(height=16),
                                ft.ElevatedButton(
                                    "Open Certificates",
                                    icon=ft.Icons.OPEN_IN_NEW,
                                    style=ft.ButtonStyle(
                                        color="#ffffff",
                                        bgcolor="#0ea5e9",
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    on_click=lambda _: page.go("/matlab"),
                                ),
                            ],
                            spacing=16,
                        ),
                    ),
                    ft.Container(
                        col={"xs": 12, "md": 4},
                        padding=ft.Padding.all(22),
                        border_radius=20,
                        bgcolor="#0f172a",
                        border=ft.Border.all(1, "#172a45"),
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Icon(ft.Icons.CODE, color="#0ea5e9", size=22),
                                        ft.Text("GitHub", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ],
                                    spacing=10,
                                ),
                                ft.Text("https://github.com/ceubilly", size=13, color="#94a3b8", selectable=True),
                                ft.Container(height=16),
                                ft.ElevatedButton(
                                    "Open GitHub",
                                    icon=ft.Icons.OPEN_IN_NEW,
                                    style=ft.ButtonStyle(
                                        color="#ffffff",
                                        bgcolor="#0ea5e9",
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                    on_click=lambda _: page.launch_url("https://github.com/ceubilly"),
                                ),
                            ],
                            spacing=16,
                        ),
                    ),
                ],
                spacing=20,
                run_spacing=20,
            ),
        ],
        spacing=18,
        scroll=ft.ScrollMode.AUTO,
    )

