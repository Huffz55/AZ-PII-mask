# Azerbaijani PII Masker & Reversible Encoder

A tiny Python script that finds personally‑identifiable information (PII) in Azerbaijani text and either **masks** it with placeholders or **encodes** it in reversible Base‑64 tokens.

> **Why?** Share logs, datasets, or demo sentences publicly without leaking real phone numbers, addresses, e‑mails, dates of birth, card numbers, IPs or ID numbers.

---

## 🚀 Quick Start

```bash
# clone or download the repo
python pii_masker.py                   # runs the demo inside the script
```

No external dependencies – uses only Python 3 standard library (`re`, `json`, `base64`).

---

## 🛠️ How It Works

1. **Regex dictionary** (`regex = { … }`) targets eight PII types:

   * `ADDRESS`, `NAME`, `DOB`, `EMAIL`, `PHONE`, `IP`, `CARD`, `ID`
2. **Masking Mode** – every match is replaced by `[TYPE]`.
3. **Encoding Mode** – every match is replaced by `[TYPE:BASE64]`, and the cleartext is stored into `decodedMap.json` for later reversal.

> Switch between modes by commenting / uncommenting the relevant section in `pii_masker.py` (see the code comments).

---

## 📄 Example

### Input text

```text
Salam, mənim adım Elçin Məmmədovdur. Mən 15/03/1989-cu ildə anadan olmuşam.
E-poçt ünvanım elchin.mammadov+job@gmail.com və telefon nömrəm +994 (50) 123-45-67-dir.
Hal-hazırda Bakı şəhəri, Nizami küçəsi 25 ünvanında yaşayıram.
Zəhmət olmasa bu IP ünvanından istifadə edin: 192.168.0.101.
Kredit kartımın nömrəsi belədir: 4111 1111 1111 1111.
```

### 1 · Masking mode

```text
Salam, mənim adım [NAME]dur. Mən [DOB]-cu ildə anadan olmuşam.
E-poçt ünvanım [EMAIL] və telefon nömrəm [PHONE]-dir.
Hal-hazırda [ADDRESS] ünvanında yaşayıram.
Zəhmət olmasa bu IP ünvanından istifadə edin: [IP].
Kredit kartımın nömrəsi belədir: [CARD].
```

### 2 · Encoding mode (reversible)

```text
Salam, mənim adım [NAME:RWzDp2luIE3Dp21tw6fDp2Rvdg==]dur. Mən [DOB:MTUvMDMvMTk4OQ==]-cu ildə anadan olmuşam.
E-poçt ünvanım [EMAIL:ZWxjaGluLm1hbW1hZG92K2pvYkBnbWFpbC5jb20=] və telefon nömrəm [PHONE:Kzk5NCAoNTApIDEyMy00NS02Nw==]-dir.
Hal-hazırda [ADDRESS:QmFrxLEgc2Vow6fDpywgTml6YW1pIGvDvHPDp3NpIDI1] ünvanında yaşayıram.
Zəhmət olmasa bu IP ünvanından istifadə edin: [IP:MTkyLjE2OC4wLjEwMQ==].
Kredit kartımın nömrəsi belədir: [CARD:NDExMSAxMTExIDExMTEgMTExMQ==].
```

`decodedMap.json` produced by the same run:

```json
{
  "NAME": "Elçin Məmmədov",
  "DOB": "15/03/1989",
  "EMAIL": "elchin.mammadov+job@gmail.com",
  "PHONE": "+994 (50) 123-45-67",
  "ADDRESS": "Bakı şəhəri, Nizami küçəsi 25",
  "IP": "192.168.0.101",
  "CARD": "4111 1111 1111 1111"
}
```

---

## 🔍 Regex Patterns

| Key       | Regex (simplified)                             | Captures                             |                       |
| --------- | ---------------------------------------------- | ------------------------------------ | --------------------- |
| `ADDRESS` | \`Bakı… (küçəsi                                | prospekti)…\`                        | Street & building no. |
| `NAME`    | Azerbaijani latin title‑case words             | Full names incl. prefixes like *Dr.* |                       |
| `DOB`     | `dd/mm/yyyy`, `dd.mm.yyyy`, `dd-mm-yyyy`       | Birth dates                          |                       |
| `EMAIL`   | Standard email                                 | -                                    |                       |
| `PHONE`   | Variations of `+994` or local format           | Mobile & landline                    |                       |
| `IP`      | `d.d.d.d`                                      | IPv4                                 |                       |
| `CARD`    | `#### #### #### ####` or `####-####-####-####` | Bank cards                           |                       |
| `ID`      | `9‒10` digits                                  | Azerbaijani ID numbers               |                       |

> You can tweak or expand these patterns in `regex` dict to fit your own data rules.

---

## 📝 License

MIT © 2025  · Feel free to use, modify, and share.

---

## 🤝 Contributing

Issues and pull requests are welcome – especially for improved regex accuracy or additional PII types.
