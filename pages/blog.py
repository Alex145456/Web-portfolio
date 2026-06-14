import flet as ft

from components.section import formula_box, info_card, page_header


POSTS = [
    {
        "title": "Confidence in Metallurgical Cost Estimation",
        "video": "https://samplelib.com/lib/preview/mp4/sample-5s.mp4",
        "summary": "A technical note explaining how reagent, energy, feed, and labour quantities combine into a defensible metallurgical process estimate.",
        "formula": "Total Cost = \u03a3(Q\u1d62 \u00d7 P\u1d62) + Overheads",
        "explanation": "Q\u1d62 is the quantity of item i, P\u1d62 is its unit price, and the summation adds every project item before overheads are included.",
    },
    {
        "title": "Mass Balance Reasoning",
        "video": "https://samplelib.com/lib/preview/mp4/sample-10s.mp4",
        "summary": "A short explanation of how mass balance supports metallurgical process checks and reduces reporting errors.",
        "formula": "Input Mass = Product Mass + Waste Mass + Losses",
        "explanation": "This relation is used to check whether measured stream outputs are physically consistent with feed inputs.",
    },
    {
        "title": "Metallurgical Recovery Calculation",
        "video": "https://samplelib.com/lib/preview/mp4/sample-15s.mp4",
        "summary": "A concept explanation for checking how much valuable product is recovered from a feed stream.",
        "formula": "Recovery (%) = (Valuable Product / Valuable Feed) \u00d7 100",
        "explanation": "Recovery measures the percentage of target material captured in the product stream instead of being lost to waste or tailings.",
    },
]


def video_insert(page: ft.Page, url: str) -> ft.Control:
    # Flet 0.85.3 does not include ft.Video / ft.VideoMedia.
    # Use a placeholder and let the user open the MP4 externally.
    return ft.Container(
        height=190,
        padding=ft.Padding.all(16),
        border_radius=8,
        bgcolor="#08182b",
        border=ft.Border.all(1, "#173554"),
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.PLAY_CIRCLE, size=36, color="#61a5ff"),
                        ft.Text(
                            "Video",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10,
                ),
                ft.Container(height=10),
                ft.Text(
                    "Inline playback is unavailable in this Flet version.",
                    size=12,
                    color="#9fb1c8",
                ),
                ft.Text(
                    url,
                    size=11,
                    color="#94a3b8",
                    selectable=True,
                ),
                ft.Container(height=12),
                ft.ElevatedButton(
                    "Open Video",
                    icon=ft.Icons.OPEN_IN_NEW,
                    style=ft.ButtonStyle(
                        color="#ffffff",
                        bgcolor="#0ea5e9",
                        shape=ft.RoundedRectangleBorder(radius=10),
                    ),
                    on_click=lambda e: page.launch_url(url),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
        ),
    )




def blog_post(page: ft.Page, post: dict) -> ft.Container:
    return ft.Container(
        padding=ft.Padding.all(18),
        border_radius=8,
        bgcolor="#0d1d31",
        border=ft.Border.all(1, "#173554"),
        content=ft.Column(
            controls=[
                ft.Text(post["title"], size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(post["summary"], size=13, color="#b6c6dc"),
                formula_box(post["formula"], post["explanation"]),
                video_insert(page, post["video"]),
            ],
            spacing=14,
        ),
    )


def build_blog_page(page: ft.Page) -> ft.Control:
    return ft.Column(
        controls=[
            page_header(
                "Technical Blog",
                "Confidence in Concepts: formulas, engineering explanations, and embedded video inserts.",
                ft.Icons.ARTICLE,
            ),
            info_card(
                "Mathematical notation",
                "The blog uses Unicode mathematical notation for reliable web rendering in Flet, including \u03a3, \u222b, subscripts, and superscripts.",
                ft.Icons.FUNCTIONS,
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(
                        "View MATLAB Certificates",
                        icon=ft.Icons.SCHOOL,
                        on_click=lambda _: page.go("/matlab"),
                        style=ft.ButtonStyle(color="#06101d", bgcolor="#f0bf63", shape=ft.RoundedRectangleBorder(radius=8)),
                    ),
                    ft.OutlinedButton(
                        "See Project Timeline",
                        icon=ft.Icons.TIMELINE,
                        on_click=lambda _: page.go("/timeline"),
                        style=ft.ButtonStyle(color="#b6c6dc", side=ft.BorderSide(1, "#2a4f7d"), shape=ft.RoundedRectangleBorder(radius=8)),
                    ),
                ],
                spacing=12,
                wrap=True,
            ),
            ft.Column(controls=[blog_post(page, post) for post in POSTS], spacing=16),
        ],
        spacing=18,
        scroll=ft.ScrollMode.AUTO,
    )
