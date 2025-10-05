from polarbadge.models.card import CardType

CARD_TYPES = {
    "cr80": CardType(
        name="CR-80",
        # Dimensions are based on Zebra ZC-100 @ 300DPI
        width_mm="54.186",
        height_mm="85.174",
        # Pixel sizes are the most important ones
        width_px=640,
        height_px=1006
    )
}
        
        
