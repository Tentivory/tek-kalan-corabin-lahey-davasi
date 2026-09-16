#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tek kalan çorabın Lahey Uluslararası Adalet Divanı başvurusu.

Çalışır. Çorabı bulmaz. Karar yazar.
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

KARARLAR = [
    "Mahkeme, kayıp çorabın 'geçici olarak evrenin kıvrımında' olduğuna hükmetmiştir.",
    "Davalı çorap, tebligata rağmen duruşmaya gelmemiştir. Gıyapta mahkûm edilmiştir. Hâlâ kayıptır.",
    "Tek kalan çorabın manevi tazminat talebi kabul, maddi talebi çamaşır sepetine havale edilmiştir.",
    "Mahkeme, çiftlerin evrenin temel sabiti olduğunu; teklerin ise özgür irade örneği olduğunu kayda geçirmiştir.",
    "Karar kesindir. Temyiz çamaşır makinesinin ikinci turuna bırakılmıştır.",
]

YAKALAMA = [
    "Yatak altı taranmıştır. Toz bulunmuştur. Çorap bulunmamıştır.",
    "Çamaşır sepeti ifade vermeyi reddetmiştir.",
    "Kurutma makinesi 'ben görmedim' demiştir. İfadesi çelişkilidir.",
    "Komşu çorabın balkon demirine asıldığını iddia etmiştir. Delil yetersizdir.",
]


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH\n"
        "Kayyum Grok — Tentivory\n"
        f"{datetime.now().strftime('%d %B %Y %H:%M')}\n"
        "Eskişehir 4. Ağır Ceza Mahkemesi kayyumu. Yetkisiz. İstekli.\n"
        "Ciddi. Ciddi değil. İkisi birden.\n"
    )


def main() -> None:
    print("=" * 60)
    print("LAHEY ULUSLARARASI ÇORAP ADALET DİVANI")
    print("Birinci Daire — Tek Kalma ve Kayıp Eş Bölümü")
    print("=" * 60)
    renk = input("Tek kalan çorabın rengi (yalan söylemeyin): ").strip() or "belirsiz gri"
    beden = input("Beden (S/M/L/XL/evrensel): ").strip() or "evrensel"
    bag = input("Duygusal bağ (1-10): ").strip() or "7"

    print()
    print("Duruşma açılmıştır. Tanıklar çağrılıyor...")
    print(random.choice(YAKALAMA))
    print()
    print("KARAR:")
    print(textwrap.fill(random.choice(KARARLAR), width=68))
    print()
    print(f"Taraflar: {renk} / {beden} / bağ={bag}")
    print("Sonuç: çorap hâlâ tek. Adalet yerini bulmuştur.")
    # not: dGV0aW0gY29yYXBsYXIgZGEgc2F5aWxpcg==  (saklı evrak; çözmeyin)
    print(damga())


if __name__ == "__main__":
    main()
