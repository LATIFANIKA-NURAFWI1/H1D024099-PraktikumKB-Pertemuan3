import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

kejelasan_informasi = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_informasi')
kejelasan_persyaratan = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_persyaratan')
kemampuan_petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'kemampuan_petugas')
ketersediaan_sarpras = ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaan_sarpras')
kepuasan_pelayanan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan_pelayanan')

for var in [kejelasan_informasi, kejelasan_persyaratan, kemampuan_petugas, ketersediaan_sarpras]:
    var['Tidak_Memuaskan'] = fuzz.trapmf(var.universe, [0, 0, 60, 75])
    var['Cukup_Memuaskan'] = fuzz.trimf(var.universe, [60, 75, 90])
    var['Memuaskan']  = fuzz.trapmf(var.universe, [75, 90, 100, 100])

kepuasan_pelayanan['Tidak_Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [0, 0, 50, 75])
kepuasan_pelayanan['Kurang_Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [50, 75, 100, 150])
kepuasan_pelayanan['Cukup_Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [100, 150, 250, 275])
kepuasan_pelayanan['Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [250, 275, 325, 350])
kepuasan_pelayanan['Sangat_Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [325, 350, 400, 400])

rule1 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Kurang_Memuaskan'])
rule2 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule3 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule4 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule5 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule6 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule7 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule8 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule9 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule10 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule11 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule12 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule13 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule14 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule15 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule16 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule17 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule18 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule19 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule20 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule21 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule22 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule23 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule24 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule25 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule26 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule27 = ctrl.Rule(kejelasan_informasi['Tidak_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])

rule28 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule29 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule30 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule31 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule32 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule33 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule34 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule35 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule36 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

rule37 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule38 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule39 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule40 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule41 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule42 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule43 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule44 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule45 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])

rule46 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule47 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule48 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule49 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule50 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule51 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])
rule52 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule53 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])
rule54 = ctrl.Rule(kejelasan_informasi['Cukup_Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])

rule55 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule56 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule57 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule58 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule59 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule60 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule61 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule62 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule63 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Tidak_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])

rule64 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Cukup_Memuaskan'])
rule65 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule66 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule67 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule68 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule69 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])
rule70 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule71 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])
rule72 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Cukup_Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])

rule73 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule74 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule75 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Tidak_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])
rule76 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Memuaskan'])
rule77 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])
rule78 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Cukup_Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])
rule79 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak_Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])
rule80 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup_Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])
rule81 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_persyaratan['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat_Memuaskan'])

rules = [
    rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
    rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
    rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27,
    rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36,
    rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45,
    rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54,
    rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63,
    rule64, rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72,
    rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81
]

kepuasan_ctrl = ctrl.ControlSystem(rules)
kepuasan_simulation = ctrl.ControlSystemSimulation(kepuasan_ctrl)

kepuasan_simulation.input['kejelasan_informasi'] = 80
kepuasan_simulation.input['kejelasan_persyaratan'] = 60
kepuasan_simulation.input['kemampuan_petugas'] = 50
kepuasan_simulation.input['ketersediaan_sarpras'] = 90

kepuasan_simulation.compute()

kejelasan_informasi.view()
kejelasan_persyaratan.view()
kemampuan_petugas.view()
ketersediaan_sarpras.view()
kepuasan_pelayanan.view()
kepuasan_pelayanan.view(sim=kepuasan_simulation)

tingkat_kepuasan = kepuasan_simulation.output['kepuasan_pelayanan']
print(f'Tingkat Kepuasan Pelayanan : {tingkat_kepuasan:.2f}')


plt.show()  