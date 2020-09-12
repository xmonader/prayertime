# prayertime
python library for calculating prayertimes and qibla direction.


## Example



```python

pt = Prayertime(31.2599, 30.0599, 2, 2010, 8, 6, Calendar.EgyptianGeneralAuthorityOfSurvey, Mazhab.Default, Season.Summer)
print(pt.get_qibla())
pt.calculate()
pt.report()
    
```

## API 
- To initialize prayertime object, you need to pass`longitude`, `latitude`, `zone`, `year`, `month`, `day`, `calendar`, `mazhab` ,`season`
- Seasons (Summer, Winter)
- Mazhab (Default, Hanafy)
- Calendar (UmmAlQuraUniv, EgyptianGeneralAuthorityOfSurvey UnivOfIslamicSciencesKarachi, IslamicSocietyOfNorthAmerica)
