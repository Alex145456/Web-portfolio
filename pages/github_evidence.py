import asyncio
import flet as ft

from components.section import info_card, page_header


BG = "#070d1a"
CARD = "#0c1526"
BORDER = "#1a2e4a"
ACCENT = "#f0a500"
CYAN = "#38bdf8"
WHITE = "#ffffff"
TEXT_P = "#c8d8ed"
TEXT_S = "#8899b4"
RADIUS = 12
REPO_URL = "https://github.com/silverna-creator/UNAM-I3691CP-buildtech-innovators-EM-lab"

COMMITS = [
    {
        "file": "commits4.png",

        "label": "commits4 — Earlier main branch commits",
        "summary_short": "Mostly setup and structural work: repo init, Prompt.md, app structure fixes and minor formatting tweaks.",
        "summary_long": "Initialized repository, added and updated Prompt.md, fixed app structure via PR #1, reverted a monolithic App.js, and applied minor formatting tweaks (\"Made things readable\", \"Added spaces\").",
        "url": REPO_URL,
    },
    {
        "file": "committs.png",

        "label": "committs — May 30, 2026 commits",
        "summary_short": "Security-focused: added safe logout paths and fixed refresh exploit by checking global DB lock status in auth routing.",
        "summary_long": "Added safe logout paths on lockdown screens to prevent state loss on refresh, and fixed a refresh exploit by checking the global database lock status inside the auth routing gate.",
        "url": REPO_URL,
    },
    {
        "file": "committs1.png",

        "label": "committs1 — Feature and infra work",
        "summary_short": "Feature and infrastructure: moisture/flotation metrics, persisted lockdown state, error boundary, read-only sample screen, technician form fixes.",
        "summary_long": "Displayed moisture and flotation metrics on dashboards; persisted system lockdown status to Firestore; added a global error boundary for operator pipeline; implemented read-only sample details screen; modularized technician registration test types; fixed Firebase Auth signOut import error.",
        "url": REPO_URL,
    },
]

PRS = [
    {
        "id": "#3",
        "title": "LogSampleScreen — Progress",
        "status": "Merged",
        "review": "Progress (17 commits merged into main) — Missing JSX fields, missing exports, missing weight/moisture/flotation display values, incorrect label layouts, and swapped inline styles for global card styles.",
        "image": "commit2.jpeg",
        "url": REPO_URL + "/pull/3",
    },
]


def commit_tile(commit: dict, page: ft.Page) -> ft.Container:
    return ft.Container(
        bgcolor=CARD,
        border_radius=RADIUS,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        border=ft.Border.all(1, BORDER),
        content=ft.Row(
            controls=[
                ft.Container(width=4, bgcolor=CYAN),
                ft.Container(
                    expand=True,
                    padding=ft.Padding.only(left=16, top=16, right=16, bottom=16),
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                width=220,
                                height=140,
                                border_radius=8,
                                bgcolor="#08182b",
                                border=ft.Border.only(left=ft.BorderSide(3, CYAN)),
                                content=(
                                    ft.Image(src=f"assets/github/{commit.get('file')}", width=220, height=140, fit="contain")
                                    if commit.get("file")
                                    else ft.Column(
                                        controls=[
                                            ft.Container(height=24),
                                            ft.Text("Screenshot", size=12, color=TEXT_S),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    )
                                ),
                            ),
                            ft.Container(width=16),
                            ft.Column(
                                expand=True,
                                spacing=10,
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                padding=ft.Padding.only(left=10, top=6, right=10, bottom=6),
                                                border_radius=6,
                                                bgcolor=BG,
                                                content=ft.Text(
                                                    commit.get("label", commit.get("hash", "")),
                                                    font_family="monospace",
                                                    size=12,
                                                    color=WHITE,
                                                ),
                                            ),
                                            ft.Container(width=12),
                                            ft.Text(
                                                commit.get("title", commit.get("label", "")),
                                                size=15,
                                                weight=ft.FontWeight.BOLD,
                                                color=WHITE,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.START,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    ft.Text(commit.get("summary_short", ""), size=12, color=TEXT_P),
                                    ft.Text(commit.get("summary_long", ""), size=12, color=TEXT_S),
                                    ft.Row(
                                        spacing=10,
                                        alignment=ft.MainAxisAlignment.END,
                                        controls=[
                                            ft.ElevatedButton(
                                                "View details",
                                                icon=ft.Icons.DESCRIPTION,
                                                on_click=lambda *args, c=commit: _open_image_dialog(
                                                    page, c.get("file")
                                                )
                                                if c.get("file")
                                                else _open_commit_dialog(page, c),
                                                style=ft.ButtonStyle(
                                                    color="#06101d",
                                                    bgcolor=ACCENT,
                                                    shape=ft.RoundedRectangleBorder(radius=8),
                                                ),
                                            ),
                                            ft.OutlinedButton(
                                                "Open on GitHub",
                                                icon=ft.Icons.OPEN_IN_NEW,
                                                on_click=lambda e, url=commit.get("url"): _open_url(page, url) if url else None,
                                                style=ft.ButtonStyle(
                                                    color=WHITE,
                                                    side=ft.BorderSide(1, CYAN),
                                                    shape=ft.RoundedRectangleBorder(radius=8),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                        spacing=16,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
            ],
        ),
    )


def _open_commit_dialog(page: ft.Page, commit: dict):
    def _close(e):
        dlg.open = False
        page.update()

    dlg = ft.AlertDialog(
        title=ft.Text(commit.get("label", "Commit details")),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Text(commit.get("summary_long", ""), size=12, color=TEXT_P),
                (ft.Image(src=f"assets/github/{commit.get('file')}", width=520, height=320, fit="contain")
                 if commit.get('file') else ft.Text("", size=0)),
            ]
        ),
        actions=(
            [
                ft.TextButton(
                    "Preview Image",
                    on_click=lambda e, src=commit.get('file'): _open_image_dialog(page, src) if src else None,
                ),
                ft.TextButton("Close", on_click=_close),
            ]
            if commit.get('file')
            else [ft.TextButton("Close", on_click=_close)]
        ),
    )
    page.dialog = dlg
    dlg.open = True
    page.update()


def _open_image_dialog(page: ft.Page, img_file: str):
    if not img_file:
        # If the image filename is missing, still open the dialog (prevents 'nothing happens').
        dlg = ft.AlertDialog(
            title=ft.Text("Preview"),
            content=ft.Container(
                width=900,
                height=650,
                alignment=ft.Alignment(0, 0),
                content=ft.Text("Image not found.", color=TEXT_S),
            ),
            actions=[ft.TextButton("Close", on_click=lambda e: _close_preview())],
        )
        page.dialog = dlg
        dlg.open = True
        page.update()
        return

    def _close_preview():
        if page.dialog:
            page.dialog.open = False
            page.update()

    def _close_img(e):
        img_dlg.open = False
        page.update()

    img_dlg = ft.AlertDialog(
        title=ft.Text("Preview"),
        modal=True,
        content=ft.Container(
            width=900,
            height=650,
            content=ft.Image(
                src=f"assets/github/{img_file}",
                width=900,
                height=650,
                fit="contain",
            ),
        ),
        actions=[ft.TextButton("Close", on_click=_close_img)],
    )
    page.dialog = img_dlg
    img_dlg.open = True
    page.update()


def _open_url(page: ft.Page, url: str):
    if not url:
        print('No URL to open')
        return
    try:
        print('Opening URL:', url)
        asyncio.create_task(page.launch_url(url))
    except Exception as ex:
        print('Failed to open URL:', ex)


def pr_tile(pr: dict, page: ft.Page) -> ft.Container:
    status_color = "#61d394" if pr["status"] == "Merged" else "#38bdf8" if pr["status"] == "Reviewed" else ACCENT
    controls = [
        ft.Container(width=4, bgcolor=status_color),
        ft.Container(
            expand=True,
            padding=ft.Padding.only(left=16, top=16, right=16, bottom=16),
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(pr["id"], size=14, weight=ft.FontWeight.BOLD, color=WHITE),
                            ft.Container(width=12),
                            ft.Container(
                                padding=ft.Padding.only(left=10, top=4, right=10, bottom=4),
                                border_radius=8,
                                bgcolor="#11283c",
                                content=ft.Text(pr["status"], size=11, weight=ft.FontWeight.BOLD, color=status_color),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Text(pr["title"], size=15, weight=ft.FontWeight.BOLD, color=WHITE),
                    ft.Text(pr["review"], size=12, color=TEXT_P),
                ],
            ),
        ),
    ]

    # If PR has an image, show a preview and a Preview button
    if pr.get("image"):
        controls.append(
            ft.Container(
                padding=ft.Padding.only(left=16, top=8, right=16, bottom=16),
                content=ft.Column(
                    spacing=8,
                    controls=[
                        ft.Image(src=f"assets/github/{pr.get('image')}", width=520, height=320, fit="contain"),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.TextButton(
                                    "Preview Image",
                                    on_click=lambda e, src=pr.get('image'): _open_image_dialog(page, src) if src else None,
                                )
                                ,
                                ft.OutlinedButton(
                                    "Open on GitHub",
                                    icon=ft.Icons.OPEN_IN_NEW,
                                    on_click=lambda e, url=pr.get('url'): _open_url(page, url) if url else None,
                                    style=ft.ButtonStyle(
                                        color=WHITE,
                                        side=ft.BorderSide(1, CYAN),
                                        shape=ft.RoundedRectangleBorder(radius=8),
                                    ),
                                )
                            ],
                        ),
                    ],
                ),
            )
        )

    return ft.Container(
        bgcolor=CARD,
        border_radius=RADIUS,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        border=ft.Border.all(1, BORDER),
        content=ft.Column(
            controls=controls,
        ),
    )


def build_github_page(page: ft.Page) -> ft.Control:
    return ft.Column(
        controls=[
            page_header(
                "GitHub Evidence",
                "Commit history and pull request logs rendered in a clean desktop portfolio layout.",
                ft.Icons.CODE,
            ),
            info_card(
                "Repository Evidence",
                "Review recent commit and pull request activity with a consistent, desktop-friendly layout.",
                ft.Icons.GITE,
            ),
            ft.Column(
                spacing=18,
                controls=[
                    ft.Text("Commit History", size=20, weight=ft.FontWeight.BOLD, color=WHITE),
                    ft.Column(
                        spacing=14,
                        controls=[commit_tile(commit, page) for commit in COMMITS],
                    ),
                    ft.Container(height=8),
                    ft.Text("Pull Request Logs", size=20, weight=ft.FontWeight.BOLD, color=WHITE),
                                ft.Column(
                                    spacing=14,
                                    controls=[pr_tile(pr, page) for pr in PRS],
                                ),
                ],
            ),
        ],
        spacing=18,
        scroll=ft.ScrollMode.AUTO,
    )
