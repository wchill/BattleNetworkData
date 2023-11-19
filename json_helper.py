import json


def main():
    chip_id = int(input("Starting id: "))
    chips = []

    while True:
        try:
            id_str = str(chip_id).rjust(3, "0")
            name = input(f"{id_str} chip name: ")

            if name == "":
                break

            element = input(f"{id_str} element: ") or chips[-1]["element"]
            attack = int(input(f"{id_str} attack: ")) or chips[-1]["attack"]
            codes = list(input(f"{id_str} codes: ").upper()) or chips[-1]["codes"]
            mb = int(input(f"{id_str} mb: ")) or chips[-1]["mb"]
            description = input(f"{id_str} desc: ") or chips[-1]["description"]

            chips.append({
                "id": id_str,
                "name": name,
                "element": element,
                "attack": attack,
                "codes": codes,
                "mb": mb,
                "description": description
            })

            chip_id += 1
        except Exception:
            pass

    with open("output.json", "w") as f:
        json.dump(chips, f)


if __name__ == "__main__":
    main()
