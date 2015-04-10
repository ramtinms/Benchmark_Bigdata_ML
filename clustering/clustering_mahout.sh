#mahout seqdirectory -c UTF-8 -i reuters -o reuters-seqfiles -xm sequential

#mahout seq2sparse -i reuters-seqfiles -o reuters-vectors -ow

#mahout seq2sparse -i reuters-seqfiles -o reuters-normalized-bigram -ow -a org.apache.lucene.analysis.core.WhitespaceAnalyzer -chunk 200 -wt tfidf -s 5 -md 3 -x 90 -ng 2 -ml 50 -seq -n 2

#mahout seq2sparse -i reuters-seqfiles -o reuters-seqfiles-sparse -wt tfidf -ng 3 -n 2 --maxDFPercent 85


# Working copy 
#+ SOME other command to filter reuters

mahout seqdirectory -i reuters-out -o reuters-out-seqdir3 -c UTF-8 -chunk 64 -xm sequential    

mahout seq2sparse -i reuters-out-seqdir3 -o reuters-out-seqdir-sparse-kmeans3 --maxDFPercent 85 --namedVector  

mahout kmeans -i reuters-out-seqdir-sparse-kmeans3/tfidf-vectors/ -c reuters-kmeans-clusters3 -o reuters-kmeans3 -dm org.apache.mahout.common.distance.CosineDistanceMeasure -x 10 -k 20 -ow --clustering 

mahout clusterdump -i reuters-kmeans3/clusters-2-final -o reuters-kmeans3/clusterdump -d reuters-out-seqdir-sparse-kmeans3/dictionary.file-0 -dt sequencefile -b 100 -n 20 --evaluate -dm org.apache.mahout.common.distance.CosineDistanceMeasure -sp 0 --pointsDir reuters-kmeans3/clusteredPoints   

