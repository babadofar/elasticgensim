export dump=../nowiki-20160822-cirrussearch-content.json.gz
export index=content

mkdir chunks
cd chunks
zcat ../$dump | split -a 10 -l 500 - $index