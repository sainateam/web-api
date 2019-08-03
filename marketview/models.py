from djongo import models

# Daily Data
class DailyData(models.Model):
    d = models.DateTimeField()      # Date
    cbr = models.IntegerField()     # Count Buy Real
    cbl = models.IntegerField()     # Count Buy Legal
    csr = models.IntegerField()     # Count Sell Real
    csl = models.IntegerField()     # Count Sell Legal
    vobr = models.IntegerField()    # Volume Buy Real
    vobl = models.IntegerField()    # Volume Buy Legal
    vosr = models.IntegerField()    # Volume Sell Real
    vosl = models.IntegerField()    # Volume Sell Legal
    vabr = models.IntegerField()    # Value Buy Real
    vabl = models.IntegerField()    # Value Buy Legal
    vasr = models.IntegerField()    # Value Sell Real
    vasl = models.IntegerField()    # Value Sell Legal
    o = models.IntegerField()       # Open Price
    h = models.IntegerField()       # High Price
    l = models.IntegerField()       # Low Price
    c = models.IntegerField()       # Close Price
    lo = models.IntegerField()      # Last Order Price  

    class Meta:
        abstract = True

# Symbol
class Symbol(models.Model):
    LVal18AFC = models.CharField(max_length=50)
    InsCode = models.CharField(max_length=20)
    InstrumentID = models.CharField(max_length=12)
    CIsin = models.CharField(max_length=12)
    Title = models.CharField(max_length=255)
    DailyDatas = models.ArrayModelField(model_container=DailyData)

class Analysis(models.Model):
    LVal18AFC = models.CharField(max_length=50)