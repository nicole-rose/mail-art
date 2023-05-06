# Mail Art Final Project
## File Map 

### Part 1: Web Scraping:
#### /scrapers
*aaa_scrape.py*
> scraped titles from Archives of American Art
>
*buffalo_scrape.py* 
> scraped pages from University of Buffalo + visited pages to scrape artwork info
>
#### /saic_scrapers
*saic_1_pages.py*
> scraped pages to visit 
>
*saic_2_info.py*
> visited pages to scrape artwork info + collected pages with errors
>
*saic_3_info.py*
> visited pages with errors 
>
#### /saic_temp_res
*saic_pages_all.json*
> list of all saic artwork pages
>
*fails.json*
> list of pages with error messages
>
*pages_skips.json*
> list of pages skipped in first scrape
>
*ids_delete.json*
>list of ids to delete from saic results
>
### Part 2: Data Cleanup
#### /cleaners
*name_cleaner.py*
>removing extra symbols from names and placing names in correct order
>
*saic_res_cleaner.py*
>getting list of IDS to delete from SAIC results 
>
*source_change.py*
>changing source field to indicate data source
>
*source_comp.py*
>comparing names in all sources to discover names that appear in multiple sources + create list of unique names 
>
### Part 3: Results 
>CSV and JSON documents of mail info from individual sources
>
>CSV with combined info from all sources used to create edges in network
>
>CSV with individual names used to create nodes in network