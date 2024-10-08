import flet as ft


class AnimationContainer:
    def __init__(self, rectangle, spring, time_text):
        self.rectangle = rectangle
        self.time_text = time_text
        self.spring = spring
        self.view = self.create_animation_container()

    def create_animation_container(self):
        animation_content = ft.Stack(
            controls=[self.rectangle, self.spring, self.time_text],
            alignment=ft.alignment.top_center,
            expand=True,
        )

        return ft.Container(
            content=animation_content,
            expand=True,
            bgcolor=ft.colors.LIGHT_GREEN,
            padding=10,
        )
