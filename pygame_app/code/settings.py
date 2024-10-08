from pygame.math import Vector2

# screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SIDE_MENU_WIDTH = 300
TILE_SIZE = 64

# graphics
PLAY_BUTTON = "pygame_app/graphics/buttons/play_button.png"
PAUSE_BUTTON = "pygame_app/graphics/buttons/pause_button.png"

REPLAY_BUTTON_1 = "pygame_app/graphics/buttons/replay_button_1.png"
REPLAY_BUTTON_2 = "pygame_app/graphics/buttons/replay_button_2.png"

MENU_BUTTON = "pygame_app/graphics/buttons/menu_button.png"

DAMPER_BUTTON = "pygame_app/graphics/buttons/damper_button.png"

SILENCER_1 = "pygame_app/graphics/silencer.png"
SILENCER_2 = "pygame_app/graphics/silencer_2.png"

WHEEL = "pygame_app/graphics/wheel.png"
DOT = "pygame_app/graphics/dot.png"
BLOCK_WHEEL = "pygame_app/graphics/block_wheel.png"

DAMPED_VIBRATIONS_IMAGE = "pygame_app/graphics/damped_vibrations.png"
FORCED_VIBRATIONS_IMAGE = "pygame_app/graphics/forced_vibrations.png"
DYNAMIC_DAMPER_IMAGE = "pygame_app/graphics/dynamic_damper.png"

GRAPH = "pygame_app/graphics/graph.png"


# Screen scale attributes
A = 0.007017543859649123
B = -3.052631578947368

C = (SCREEN_HEIGHT - 150) / 4
D = 150 - C * 150

# Language
TIME = "Czas"
START_POSITION = "Pozycja początkowa"
SPEED = "Prędkość"
SUPPRESION_LEVEL = "Tłumienie"
ELASTICITY_COEFFICIENT = "Wsp. sprężystości"
MASS = "Masa"
ANGULAR_VELOCITY = "Prędkość kątowa"
RADIUS = "Promień"
OPTIMAL_ELASCITY = "Optymalny wsp. spr."
FREQUENCY = "Częstość wymuszenia"


# sliders
SLIDER_POSITIONS = (
    (1100, 175),
    (1100, 400),
    (1100, 470),
    (1100, 540),
    (1100, 610),
    (1100, 680),
)
SLIDER_MAX = 1250
SLIDER_MIN = 1010

# overlay positions
OVERLAY_POSITIONS = {"tool": (40, SCREEN_HEIGHT - 15), "seed": (70, SCREEN_HEIGHT - 5)}

PLAYER_TOOL_OFFSET = {
    "left": Vector2(-50, 40),
    "right": Vector2(50, 40),
    "up": Vector2(0, -10),
    "down": Vector2(0, 50),
}

LAYERS = {
    "water": 0,
    "ground": 1,
    "soil": 2,
    "soil water": 3,
    "rain floor": 4,
    "house bottom": 5,
    "ground plant": 6,
    "main": 7,
    "house top": 8,
    "fruit": 9,
    "rain drops": 10,
}

APPLE_POS = {
    "Small": [(18, 17), (30, 37), (12, 50), (30, 45), (20, 30), (30, 10)],
    "Large": [(30, 24), (60, 65), (50, 50), (16, 40), (45, 50), (42, 70)],
}

GROW_SPEED = {"corn": 1, "tomato": 0.7}

SALE_PRICES = {"wood": 4, "apple": 2, "corn": 10, "tomato": 20}
PURCHASE_PRICES = {"corn": 4, "tomato": 5}
