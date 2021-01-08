
python_parser: parser.py
	python3 parser.py
	rm DATA/*_tmp.txt
clean: 
	rm DATA/*_tmp.txt