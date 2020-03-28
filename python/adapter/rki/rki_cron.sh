#!/bin/bash
rm -f *csv
wget https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.csv
mv dd4580c810204019a7b8eb3e0b329dd6_0.csv RKI_COVID19.csv
python3 rki_upload.py