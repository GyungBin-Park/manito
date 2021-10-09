from django.conf import settings
from django.db import models
from django.forms import ModelForm

# Create your models here.

class db_Kospi200(models.Model):
    stock_code = models.TextField(blank=True, null=True)
    stock_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_kospi200'

class db_jisu(models.Model):
    stock_code = models.TextField(blank=True, null=True)
    stock_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_jisu'

        def __str__(self):
            return "종목 코드 : "+self.stock_code+", 종목명 : "+self.stock_name


class stock_info(models.Model):
    code_num = models.TextField(blank=True, null=True)
    code_name = models.TextField(blank=True, null=True)
    stk_dit_cd = models.BigIntegerField(blank=True, null=True)
    sector = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_info'


class db_interaction(models.Model):
    date = models.TextField(blank=True, null=True)
    code_name = models.TextField(blank=True, null=True)
    code_num = models.IntegerField()
    open = models.BigIntegerField(blank=True, null=True)
    high = models.BigIntegerField(blank=True, null=True)
    low = models.BigIntegerField(blank=True, null=True)
    close = models.BigIntegerField(blank=True, null=True)
    volumn = models.BigIntegerField(blank=True, null=True)
    ma20 = models.FloatField(blank=True, null=True)
    stddev = models.FloatField(blank=True, null=True)
    upper_b = models.FloatField(blank=True, null=True)
    lower_b = models.FloatField(blank=True, null=True)
    percent_b = models.FloatField(blank=True, null=True)
    bandwidth = models.FloatField(blank=True, null=True)
    macd_short = models.FloatField(blank=True, null=True)
    macd_long = models.FloatField(blank=True, null=True)
    macd = models.FloatField(blank=True, null=True)
    macd_signal = models.FloatField(blank=True, null=True)
    market_cap = models.BigIntegerField(blank=True, null=True)
    trading_volume = models.BigIntegerField(blank=True, null=True)
    out_share = models.BigIntegerField(blank=True, null=True)
    ins_buy = models.FloatField(blank=True, null=True)
    for_buy = models.FloatField(blank=True, null=True)
    ins_sell = models.FloatField(blank=True, null=True)
    for_sell = models.FloatField(blank=True, null=True)
    au = models.FloatField(blank=True, null=True)
    ad = models.FloatField(blank=True, null=True)
    rs = models.FloatField(blank=True, null=True)
    rsi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'db_interaction'


class kospi200_list(models.Model):
    code_name = models.TextField(blank=True, null=True)
    close = models.TextField(blank=True, null=True)
    diff = models.TextField(blank=True, null=True)
    per = models.TextField(blank=True, null=True)
    volume = models.TextField(blank=True, null=True)
    amount = models.TextField(blank=True, null=True)
    market_cap = models.TextField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'kospi200_list'

class f_summary(models.Model):
    id = models.AutoField(primary_key=True)
    sale = models.FloatField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    profit_a = models.FloatField(blank=True, null=True)
    ni = models.FloatField(db_column='Ni', blank=True, null=True)  # Field name made lowercase.
    ni_sh = models.FloatField(db_column='Ni_sh', blank=True, null=True)  # Field name made lowercase.
    ni_nsh = models.FloatField(db_column='Ni_nsh', blank=True, null=True)  # Field name made lowercase.
    ta = models.FloatField(db_column='TA', blank=True, null=True)  # Field name made lowercase.
    td = models.FloatField(db_column='TD', blank=True, null=True)  # Field name made lowercase.
    te = models.FloatField(db_column='TE', blank=True, null=True)  # Field name made lowercase.
    con_sh = models.FloatField(blank=True, null=True)
    con_nsh = models.FloatField(blank=True, null=True)
    cap = models.FloatField(blank=True, null=True)
    debt_r = models.FloatField(blank=True, null=True)
    reten_r = models.FloatField(blank=True, null=True)
    margin_r = models.FloatField(blank=True, null=True)
    profit_sh = models.FloatField(blank=True, null=True)
    roa = models.FloatField(db_column='ROA', blank=True, null=True)  # Field name made lowercase.
    roe = models.FloatField(db_column='ROE', blank=True, null=True)  # Field name made lowercase.
    eps = models.FloatField(db_column='EPS', blank=True, null=True)  # Field name made lowercase.
    bps = models.FloatField(db_column='BPS', blank=True, null=True)  # Field name made lowercase.
    dps = models.FloatField(db_column='DPS', blank=True, null=True)  # Field name made lowercase.
    per = models.FloatField(db_column='PER', blank=True, null=True)  # Field name made lowercase.
    pbr = models.FloatField(db_column='PBR', blank=True, null=True)  # Field name made lowercase.
    num_sh = models.FloatField(db_column='Num_sh', blank=True, null=True)  # Field name made lowercase.
    div_income = models.FloatField(db_column='Div_income', blank=True, null=True)  # Field name made lowercase.
    code_num = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_summary'



class concensus(models.Model):
    id = models.AutoField(primary_key=True)
    code_num = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    target_prc = models.BigIntegerField(db_column='TARGET_PRC', blank=True, null=True)  # Field name made lowercase.
    recom_cd = models.FloatField(db_column='RECOM_CD', blank=True, null=True)  # Field name made lowercase.
    inst_nm = models.BigIntegerField(db_column='INST_NM', blank=True, null=True)  # Field name made lowercase.
    close = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concensus'