__description__ = """downloads the latest EJP exports from the bucket to 
./thisdir/downloads/<ymd>/queryname.csv"""
__author__ = "Luke Skibinski <l.skibinski@elifesciences.org>"

import os, sys
from os.path import join
from datetime import datetime

import logging
logging.basicConfig
LOG = logging.getLogger(__name__)

THIS_DIR = os.path.realpath(os.path.dirname(sys.argv[0]))
BUCKET = "elife-ejp-ftp"
QUERIES = """ejp_query_tool_query_id_134_15c)_Accepted_Paper_Corresponding_Authors_<ymd>_eLife.csv
ejp_query_tool_query_id_152_15a)_Accepted_Paper_Details_<ymd>_eLife.csv
ejp_query_tool_query_id_158_15b)_Accepted_Paper_Details_<ymd>_eLife.csv
ejp_query_tool_query_id_176_POA_Manuscript_<ymd>_eLife.csv
ejp_query_tool_query_id_177_POA_Author_<ymd>_eLife.csv
ejp_query_tool_query_id_178_POA_License_<ymd>_eLife.csv
ejp_query_tool_query_id_179_POA_Subject_Area_<ymd>_eLife.csv
ejp_query_tool_query_id_180_POA_Received_<ymd>_eLife.csv
ejp_query_tool_query_id_182_POA_Research_Organism_<ymd>_eLife.csv
ejp_query_tool_query_id_190_Dashboard_-_Submission_Volume_<ymd>_eLife.csv
ejp_query_tool_query_id_191_POA_Title_<ymd>_eLife.csv
ejp_query_tool_query_id_196_POA_Abstract_<ymd>_eLife.csv
ejp_query_tool_query_id_209_SQL_Initial_<ymd>_eLife.csv
ejp_query_tool_query_id_210_SQL_Full_<ymd>_eLife.csv
ejp_query_tool_query_id_211_SQL_Rev1_<ymd>_eLife.csv
ejp_query_tool_query_id_212_SQL_Rev2_<ymd>_eLife.csv
ejp_query_tool_query_id_213_SQL_Rev3_<ymd>_eLife.csv
ejp_query_tool_query_id_214_SQL_Rev4_<ymd>_eLife.csv
ejp_query_tool_query_id_218_SQL_Types_<ymd>_eLife.csv
ejp_query_tool_query_id_221_SQL_Senior_Editor_1_<ymd>_eLife.csv
ejp_query_tool_query_id_222_SQL_Reviewing_Editor_<ymd>_eLife.csv
ejp_query_tool_query_id_226_POA_Keywords_<ymd>_eLife.csv
ejp_query_tool_query_id_240_SQL_Types_Full_<ymd>_eLife.csv
ejp_query_tool_query_id_241_SQL_Types_Rev1_<ymd>_eLife.csv
ejp_query_tool_query_id_242_POA_Group_Authors_<ymd>_eLife.csv
ejp_query_tool_query_id_245_SQL_Types_Rev2_<ymd>_eLife.csv
ejp_query_tool_query_id_246_SQL_Types_Rev3_<ymd>_eLife.csv
ejp_query_tool_query_id_247_SQL_Senior_Editor_2_<ymd>_eLife.csv
ejp_query_tool_query_id_248_SQL_Senior_Editor_3_<ymd>_eLife.csv
ejp_query_tool_query_id_250_SQL_Country_1_<ymd>_eLife.csv
ejp_query_tool_query_id_252_SQL_Country_2_<ymd>_eLife.csv
ejp_query_tool_query_id_253_SQL_Country_3_<ymd>_eLife.csv
ejp_query_tool_query_id_256_SQL_Appeals_Rev3_<ymd>_eLife.csv
ejp_query_tool_query_id_298_SQL_Institution_1_<ymd>_eLife.csv
ejp_query_tool_query_id_300_SQL_Institution_3_<ymd>_eLife.csv
ejp_query_tool_query_id_41_04e)_DEs_assigned_<ymd>_eLife.csv""".splitlines()

def ymd(dt=None):
    if not dt:
        dt = datetime.now()
    return dt.strftime("%Y_%m_%d")

def download(src, dest):
    import boto3
    s3 = boto3.resource('s3')
    LOG.info("fetching %r", src)
    os.system("mkdir -p %s" % os.path.dirname(dest))
    s3.meta.client.download_file(BUCKET, src, dest)
    return dest

def queries_for(dtstr):
    return map(lambda line: line.replace('<ymd>', dtstr), QUERIES)

def main():
    today = ymd()
    file_list = queries_for(today)
    dest = join(THIS_DIR, "downloads", today)
    to_download = map(lambda q: (q, join(dest, q)), file_list)
    to_download = filter(lambda p: not os.path.exists(p[1]), to_download)
    results = [download(*p) for p in to_download]
    print 'downloaded %s files to %s' % (len(results), dest)

if __name__ == '__main__':
    main()
