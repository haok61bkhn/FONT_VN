import glob
import tqdm
fonts=glob.glob("font/*")
from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)
string = "Tôi có MỘT CON CHÓ biết QUẪY và vẩy đuôi, chó như MÉO , NGU NGŨ NGÚ NGỤ "
# The generators use the same arguments as the CLI, only as parameters
for font in fonts:
    generator = GeneratorFromStrings(
        [string],
        blur=1,
        count=1,
        random_blur=True,
        background_type=3,
        random_skew=True,
        space_width=2,
        size=32,
        character_spacing=1,
        fit=False,
        alignment=3,
        #text_color="#a07081",
        fonts=[font],
        image_dir="./background",
    )

    d=0
    for img, lbl in tqdm.tqdm(generator): 
        img.save("testFont/"+font.split("/")[-1]+".jpg")
        