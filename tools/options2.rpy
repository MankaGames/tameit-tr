init -1:
    python hide:
        config.developer = True
        
        config.rollback_enabled = True
        config.rollback_length = 20
        
        
label scene_debug:
    menu:
        "Phrase length test (unicode decode)":
            jump scene_examples_translation
        "Phrase length test (plain text)":
            jump scene_examples_translation_plain
        "Unlock all chapters":
            $ progress.unlock_chapters()
            "Done"
            jump scene_debug
            
            
label scene_examples_translation:

    python:
        example_text_translation = renpy.input("Text").decode('unicode_escape')

    lee "[example_text_translation]"

jump scene_examples_translation

label scene_examples_translation_plain:

    python:
        example_text_translation = renpy.input("Text")

    lee "[example_text_translation]"

jump scene_examples_translation_plain