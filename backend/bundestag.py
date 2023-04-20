import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime
def load_mdb_data(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    mdb_data = [extract_mdb_data(mdb) for mdb in root.findall('MDB')]
    df = pd.DataFrame(mdb_data)
    return df
  
def extract_mdb_data(mdb):
    data = {}
    namen = mdb.find('NAMEN')
    biografische_angaben = mdb.find('BIOGRAFISCHE_ANGABEN')
    wp_list = [wp.text for wp in mdb.findall('.//WAHLPERIODE/WP')]
    data.update({'ID': mdb.find('ID').text,
                 'NACHNAME': namen.find('NAME/NACHNAME').text,
                 'VORNAME': namen.find('NAME/VORNAME').text,
                 'ORTSZUSATZ': namen.find('NAME/ORTSZUSATZ').text,
                 'ADEL': namen.find('NAME/ADEL').text,
                 'PRAEFIX': namen.find('NAME/PRAEFIX').text,
                 'ANREDE_TITEL': namen.find('NAME/ANREDE_TITEL').text,
                 'AKAD_TITEL': namen.find('NAME/AKAD_TITEL').text,
                 'HISTORIE_VON': namen.find('NAME/HISTORIE_VON').text,
                 'HISTORIE_BIS': namen.find('NAME/HISTORIE_BIS').text,
                 'GEBURTSDATUM': biografische_angaben.find('GEBURTSDATUM').text,
                 'GEBURTSORT': biografische_angaben.find('GEBURTSORT').text,
                 'GEBURTSLAND': biografische_angaben.find('GEBURTSLAND').text,
                 'STERBEDATUM': biografische_angaben.find('STERBEDATUM').text,
                 'GESCHLECHT': biografische_angaben.find('GESCHLECHT').text,
                 'FAMILIENSTAND': biografische_angaben.find('FAMILIENSTAND').text,
                 'RELIGION': biografische_angaben.find('RELIGION').text,
                 'BERUF': biografische_angaben.find('BERUF').text,
                 'PARTEI_KURZ': biografische_angaben.find('PARTEI_KURZ').text,
                 'VITA_KURZ': biografische_angaben.find('VITA_KURZ').text,
                 'WP_NR': wp_list})
    return data
  
def get_bundestag(xml_file, wp="20"):  
    df = load_mdb_data(xml_file)
    wanted_data = ['VORNAME', 'NACHNAME', 'VITA_KURZ', 'PARTEI_KURZ', 'GEBURTSDATUM', 'STERBEDATUM', 'GESCHLECHT', 'GEBURTSLAND','BERUF']
    aktuell_bt = df[df['WP_NR'].apply(lambda x: True if wp in x else False)][wanted_data]
    aktuell_bt.dropna(inplace=True, subset="VITA_KURZ")
    aktuell_bt['ALTER'] = aktuell_bt.apply(lambda x: (datetime.now() - pd.to_datetime(x['GEBURTSDATUM'], format='%d.%m.%Y')).days / 365.25 if pd.isnull(x['STERBEDATUM']) else (pd.to_datetime(pd.Timestamp(x['STERBEDATUM']), format='%d.%m.%Y') - pd.to_datetime(x['GEBURTSDATUM'], format='%d.%m.%Y')).days / 365.25, axis=1)
    return aktuell_bt

def anzahl_von(xml_file, suche_nach, wp="20") -> int:
    bt_wp = get_bundestag(xml_file, wp) 
    count = bt_wp.query(f'VITA_KURZ.str.contains("{suche_nach}")', engine='python')["VITA_KURZ"].count()
    return count if count > 0 else "Es gibt Keine"

def abge_name_list(xml_file, suche_nach, wp="20", alter=False, vorname=True, nachname=True, gedatum=False, sterbdatum=False, geschlecht=False, geburtsland=False, beruf=False):
    bt_wp = get_bundestag(xml_file, wp) 
    result = bt_wp.query(f'VITA_KURZ.str.contains("{suche_nach}")', engine='python')
    columns = []
    if vorname:
      columns.append("VORNAME")
    if nachname: 
      columns.append("NACHNAME")
    if alter:
      columns.append("ALTER")
    if gedatum:
      columns.append("GEBURTSDATUM")
    if sterbdatum:
      columns.append("STERBEDATUM")
    if geschlecht:
      columns.append("GESCHLECHT")
    if geburtsland:
      columns.append("GEBURTSLAND")
    if beruf:
      columns.append("BERUF")
    return result[columns].to_string(index=False, header=False) if result.empty == False else "Es gibt Keine"