from SimpleAudioIndexer import SimpleAudioIndexer as sai

indexer = sai(mode="ibm", src_dir="SRC_DIR", username_ibm="ishmeet245@gmail.com", password_ibm="Waheguru@99")
indexer.index_audio()

#indexer.save_indexed_audio("{}/indexed_audio".format(indexer.src_dir))
#indexer.load_indexed_audio("{}/indexed_audio.txt".format(indexer.src_dir))

print(indexer.get_timestamps())

searcher = indexer.search_gen(query="hello")
print(next(searcher))
