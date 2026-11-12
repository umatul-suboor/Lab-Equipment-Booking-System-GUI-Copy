EQUIPMENT = {
    "1": {"name": "Projector", "available": 3},
    "2": {"name": "Laptop", "available": 5},
    "3": {"name": "HDMI Cable", "available": 10},
    "4": {"name": "Microphone", "available": 2},
}


def get_equipment():
    return EQUIPMENT


def display_equipment():
    print("\nAvailable Laboratory Equipment:")
    print("-" * 45)
    for equipment_id, item in EQUIPMENT.items():
        print(
            f"{equipment_id}. {item['name']} "
            f"- Available: {item['available']}"
        )


def reset_equipment():
    EQUIPMENT.clear()
    EQUIPMENT.update({
        "1": {"name": "Projector", "available": 3},
        "2": {"name": "Laptop", "available": 5},
        "3": {"name": "HDMI Cable", "available": 10},
        "4": {"name": "Microphone", "available": 2},
    })
