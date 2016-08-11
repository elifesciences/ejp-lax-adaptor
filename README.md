# ejp-scraper

Transforms the report generated [here](https://github.com/elifesciences/eLife-Reporting-SQL)
into a more compatible format for [Lax](https://github.com/elifesciences/lax)

This application is managed as part of the [Lax adaptors](https://github.com/elifesciences/lax-formula).

## installation

    ./install.sh

## report scraping

James' work already generates a database that can be inspected directly as well
as a report that is used for submission metrics.

It's this report that is used as input to the scraper:

    source venv/bin/activate.sh
    python ./src/ejp_scraper.py /path/to/report.csv

## report data download

eLife receives dumps of data from views of the EJP database into an S3 bucket.

This data is then processed into a single database using this [here](https://github.com/elifesciences/eLife-Reporting-SQL). 

The files themselves can be downloaded in bulk without having to generate a 
report with:

    source venv/bin/activate.sh
    python latest_queries.py

## Copyright & Licence

Copyright 2016 eLife Sciences. Licensed under the [GPLv3](LICENCE.txt)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

