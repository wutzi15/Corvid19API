# Planning of DB Struktures

### Cases
| rows | datatype | comment |
| ------------ | ------------ | ------------ |
| date | datetime | - |
| longditude | float | - |
| latitude | flat | - |
| area | Polygon | - |
| infected | long | - |
| dead | long | - |
| recovered | long | - |
| source | Source | - |

### Events
| rows | datatype | comment |
| ------------ | ------------ | ------------ |
| date | datetime | - |
| longditude | float | - |
| latitude | flat | - |
| category | string | Ausgangssperre, Flug Verbot etc. |
| effect | ? | Auswirkungen auf Wachstumszahlen |
| type | string | Natürlich / Regierung / Gesellschaft |

### Sources
| rows | datatype | comment |
| ------------ | ------------ | ------------ |
| name | String | - |
| url | String | - |