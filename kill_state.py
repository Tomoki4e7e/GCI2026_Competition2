# Pythonで修正するスクリプト

import json

with open("baseline_advanced.ipynb", "r", encoding="utf-8") as f:
    nb = json.load(f)

# metadata.widgets を削除
if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]
    print("widgets メタデータを削除しました")

with open("baseline_advanced.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("保存完了")
