init -1:
    python hide:
        config.developer = True
        
        config.rollback_enabled = True
        config.rollback_length = 20
        
        
label scene_debug:
    menu:
        "Phrase length test":
            jump scene_examples_translation
            
            
label scene_examples_translation:

    python:
        example_text_translation = renpy.input("Text").decode('unicode_escape')

    lee "[example_text_translation]"

jump scene_examples_translation