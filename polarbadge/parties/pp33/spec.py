import os

from polarbadge.card.constants import CARD_TYPES
from polarbadge.models.card import Code2DBox, Font, TextBox, Image, ImageBox, Design, ExternalFontFamily

# Dir or current file
BASE_PATH = os.path.dirname(os.path.realpath(__file__))

FONT_QUICKSAND = ExternalFontFamily(
    family_name="Quicksand",
    path=os.path.join(BASE_PATH, "fonts/Quicksand/Quicksand-VariableFont_wght.ttf")
)


design = Design(
    card=CARD_TYPES["cr80"],
    base_font=Font(
        family=FONT_QUICKSAND,
        size_pt=18,
        color="ffffff"
    ),
    orientation="portrait",
    background_png=Image(path=os.path.join(BASE_PATH, "background.png")),
    foreground_png=Image(path=os.path.join(BASE_PATH, "foreground.png")),
    image_profile=ImageBox(
        width_mm="22.857",
        height_mm="22.857",
        anchor_x_mm="15.738",
        anchor_y_mm="20.921"
    ),
    text_nick=TextBox(
        width_mm="35.0",
        height_mm="3.440",
        anchor_x_mm="9.696",
        anchor_y_mm="53.822",
        font_override=Font(
            family=FONT_QUICKSAND,
            size_pt="13",
            color="ffffff"
        )
    ),
    text_name=TextBox(
        width_mm="35.0",
        height_mm="2.004",
        anchor_x_mm="9.696",
        anchor_y_mm="59.340",
        font_override=Font(
            family=FONT_QUICKSAND,
            size_pt="8",
            color="ffffff"
        )
    ),
    text_crew=TextBox(
        width_mm="35.0",
        height_mm="0.603",
        anchor_x_mm="9.696",
        anchor_y_mm="65.523",
        font_override=Font(
            family=FONT_QUICKSAND,
            size_pt="12",
            color="ffffff"
        )
    ),
    code_2d_box=Code2DBox(
        id_text_font=Font(
            family=FONT_QUICKSAND,
            size_pt="5.5",
            color="ffffff"
        ),
        size_mm="5",
        anchor_x_mm="3",
        anchor_y_mm="3"
    )
)
