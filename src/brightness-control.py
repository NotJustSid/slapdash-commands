import screen_brightness_control as sbc
import util.slap_utils as su
import json

brightness_levels = [0, 25, 50, 75, 100]

query = su.get_arg("query", None)

if query is None:
    print(json.dumps({
        "view": {
            "title": "Choose brightness level",
            "type": "form",
            "fields": [
                {
                    "type": "select",
                    "id": "query",
                    "label": "Brightness",
                    "options": [f"{level}" for level in brightness_levels]
                }
            ]
        }
    }))
else:
    sbc.set_brightness(int(query))