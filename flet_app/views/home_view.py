import flet as ft
from i18n.language import language
import asyncio

from flet_app.components.selection_bar import SelectionBar
from flet_app.components.side_bar import SideBar
from flet_app.components.animation_container import AnimationContainer
from flet_app.components.graph_container import GraphContainer

from flet_app.classes.animation import DampedVibrationAnimator


def home_view(page: ft.Page):
    page.title = language.get("page_title")

    rectangle = ft.Container(
        bgcolor=ft.colors.BLACK,
        width=200,
        height=100,
        top=20,
    )

    time_text = ft.Text(
        value="0.00",
        color=ft.colors.WHITE,
        size=16,
        left=10,
        top=10,
    )

    spring_image_container = ft.Container(
        content=ft.Image(src="/spring.png", fit=ft.ImageFit.FILL),
        width=100,
        height=300,
    )

    animation_container = AnimationContainer(
        rectangle, spring_image_container, time_text
    )
    

    def change_language(e):
        selected_lang_code = selection_bar.language_dropdown.value
        language.set_language(selected_lang_code)
        page.clean()
        home_view(page)

    def change_vibration_type(e):
        selected_vibration_type = selection_bar.vibration_type_dropdown.value
        side_bar.update_vibration_type(selected_vibration_type)

    selection_bar = SelectionBar(
        on_language_change=change_language,
        on_vibration_type_change=change_vibration_type,
    )

    initial_vibration_type = selection_bar.vibration_type_dropdown.value
    side_bar = SideBar(selected_vibration_type=initial_vibration_type)

    graph_container = GraphContainer()
    print(side_bar.sliders_dict["damped_vibrations"]["damping_coefficient"])

    right_side = ft.Row(
        controls=[
            ft.Container(content=side_bar.view, width=400),
            ft.Container(content=animation_container.view, expand=True),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
    )

    layout = ft.Column(
        controls=[
            selection_bar.view,
            ft.Row(
                controls=[
                    ft.Container(content=right_side, expand=True),
                    ft.Container(content=graph_container.view, expand=True),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            ),
        ],
        expand=True,
    )

    animation = DampedVibrationAnimator(
        rectangle,
        side_bar.sliders_dict,
        time_text,
        spring_image_container,
        graph_container,
    )
    side_bar.animation = animation

    page.add(layout)
