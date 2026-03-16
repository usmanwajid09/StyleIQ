import glob, shutil, os

src = r"C:\Users\shani\.gemini\antigravity\brain\13681cc9-a179-430d-a97c-38946266a37a"
dst = r"C:\Data\Wardrobe\images"
os.makedirs(dst, exist_ok=True)

mapping = {
    "cl_blazer_*.png": "blazer.png",
    "cl_chinos_*.png": "chinos.png",
    "cl_evening_dress_*.png": "evening_dress.png",
    "cl_gold_jacket_*.png": "gold_jacket.png",
    "cl_denim_*.png": "denim.png",
    "cl_summer_dress_*.png": "summer_dress.png",
}
for pat, name in mapping.items():
    files = glob.glob(os.path.join(src, pat))
    if files:
        shutil.copy(files[0], os.path.join(dst, name))
        print(f"Copied {files[0]} -> {name}")
print("done")
