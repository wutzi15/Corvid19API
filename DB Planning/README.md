# Planning of DB Struktures

### Cases
| rows | datatype | comment |
| ------------ | ------------ | ------------ |
| _id | ObjectId | - |
| date | datetime | - |
| adm | Array [adm0, adm1, adm2, ...]  | like [Boundaries](https://www.mapbox.com/boundaries/)
| ageRange | Array [lower: Int, upper: Int] | Agerange that people are |
| infected | long | - |
| dead | long | - |
| recovered | long | - |
| tested | long | - |
| source | Source | - |

### Measures
| rows | datatype | comment |
| ------------ | ------------ | ------------ |
| _id | ObjectId | - |
| date | datetime | - |
| adm | Array [adm0, adm1, adm2, ...]  | like [Boundaries](https://www.mapbox.com/boundaries/)
| border_control | Boolean | - |
| home_office | Boolean | - |
| closure_leisureandbars | Boolean | - |
| lockdown | Boolean | - |
| schools_closed | Boolean | - |
| traveller_quarantine | Boolean | - |
| priamry_residence | Boolean | - |
| test_limitations | Boolean | - |
| source | Source | - |

### Sources
| rows | datatype | comment |
| ------------ | ------------ | ------------ |
| name | String | - |
| url | String | - |
