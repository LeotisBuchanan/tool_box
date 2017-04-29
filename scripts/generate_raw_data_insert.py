import glob
import sys
from string import Template 

def format_date(pdte):
   pdte= pdte.replace("\"", "")
   s = pdte.split(" ")
   if(len(s) < 2):
      return None
   dte = s[0].split("/")
   tme = s[1]
   day, month, yyyy = dte
   frmt_dt = yyyy + "-" + month + "-" + day + " " + tme
   return frmt_dt


def main(data_dir, database):
   sql_template = Template("""INSERT INTO RAW_DATA (pickup_date_time,lat, lon, base) VALUES('$PICKUP_DT', $LAT, $LON, $BASE);""")
   print("USE uber;")
   data_files_path = glob.glob(data_dir+ "*.csv")
   for path in data_files_path:
      with open(path, 'r') as f:
         next(f)
         for line in f:
            fields = line.split(",")
            if len(fields) < 4:
               continue
            pickup_dt = format_date(fields[0])
            if pickup_dt is None:
               continue 
            lat = fields[1]
            lon = fields[2]
            base = fields[3]
            insert_sql = sql_template.substitute(PICKUP_DT = pickup_dt,
                                    LAT=lat,
                                    LON=lon,
                                    BASE=base)
            print(insert_sql)

                           
if __name__ == "__main__":
    data_directory =sys.argv[1]
    database = sys.argv[2]
    main(data_directory, database)
