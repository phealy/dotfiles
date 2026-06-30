-- Input configuration

hl.config({
    input = {
        accel_profile = "flat",
        touchpad = {
            natural_scroll = true,  -- Enables natural scrolling
            tap_to_click = true,    -- Optional: Enables tap-to-click
        },
    },
})

hl.gesture({ fingers = 4, direction = "horizontal", action = "workspace" })
--hl.gesture({ fingers = 3, direction = "down",       action = "close" })
--hl.gesture({ fingers = 3, direction = "up",         action = "fullscreen" })
--hl.gesture({ fingers = 3, direction = "left",       action = "float" })
