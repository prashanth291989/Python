import searcher
import indexer
d= indexer.process_data("raw_data.txt","fortunes_shelve")
searcher.search("fortunes_shelve")