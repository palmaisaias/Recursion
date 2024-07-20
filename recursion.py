def please_find(files, target):
    for item in files:
        if isinstance(item, list):  # if the item is a 'folder'
            if please_find(item, target):  # recursively search in the 'folder'
                return True
        elif item == target:  # if the item is NOT a 'folder' but rather is the target file
            print("HOORAY...we found")
            return True
    return False  # return False if the target is not found in the current folder

file_system = [
    [
        "nothing.txt",
        "dog_pic.png",
        [
            "secret_plan.pdf"
        ]
    ],
    "notion.app",
    "slack.app",
    [
        "fun.txt",
        [
            "meaningless_file.txt",
            "chicken_dinner.txt"
        ],
        "not_fun.txt"
    ],
    "zoom.app"
]

target = "chicken_dinner.txt"

please_find(file_system, target)
