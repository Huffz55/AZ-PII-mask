import re
import json
import base64



text="""Salam, mənim ünvanım Bakı şəhəri, Səməd küçəsidir. Mənə +994 51 442 21 22 nömrəsindən zəng edə bilərsiniz, adım 05.03.2009"""

regex = {
        "ADDRESS":r"(?:AZ\d{4},\s*)?(?:Bakı(?:\sşəhəri(?:n(?:də)?)?)?,?\s*)?(?:(?:\w+ rayonu),\s*)?(?:[\wəçşığöüƏÇŞİĞÜÖ\s]+?(?:küçəsi|prospekti))\s+\d{1,3}(?:,\s*mənzil\s+\d{1,3})?","NAME":r"\b[A-ZƏÇŞİĞÖÜ][a-zəçşıöüğ]+(?:\s[A-ZƏÇŞİĞÖÜ][a-zəçşıöüğ]+){1,2}\b",
         "DOB":r"\d{2}/\d{2}/\d{4}|\d{2}\.\d{2}\.\d{4}|\d{2}-\d{2}-\d{4}",
         "EMAIL":r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
         "PHONE":r"\+\d{3}\s\(\d{2}\)\s\d{3}-\d{2}-\d{2}|\d{3}\s\d{3}\s\d{2}\s\d{2}|\(\d{3}\)\s\d{3}-\d{2}-\d{2}|\+\d{3}\s\d{2}\s\d{3}\s\d{2}\s\d{2}|\+\d{3}\s\(\d{2}\)\s\d{3}\s\d{2}\s\d{2}",
         "IP": r"\d+\.\d+\.\d+\.\d+",
         "CARD":r"\d{4}\s\d{4}\s\d{4}\s\d{4}|\d{4}-\d{4}-\d{4}-\d{4}",
         "ID":r"\b(\d{9,10}\b)"    
         }
print("\n\n")

masking=text
decodedMap={}
for key,pattern in regex.items():
    masking=re.sub(pattern, f"[{key}]",masking)
print(f"Maskeli metin \n {masking}")

print("\nBase64 kodlama\n")

Bbase64=text
for key,pattern in regex.items():
    matches=re.findall(pattern,text)
    for match in matches:
        encoded=base64.b64encode(match.encode()).decode()
        placeholder = f"[{key}:{encoded}]"
        Bbase64=Bbase64.replace(match,placeholder)
        decodedMap[key]=match
print(Bbase64)

with open("decodedMap.json", "w", encoding="utf-8") as d: 
    json.dump(decodedMap, d, ensure_ascii=False, indent=2)
