This folder contains python3 source code for running CLEVER - all clinical concept extractor

sequencer.py - Takes user input files(header, lexicon, meta and notes) and determines concept sequences based on main concept or CUI 464 lines

organize.py - creates intermediate extraction.tsv files 35 lines

step3fcn.py - labels and tags parts of the concept sequences including punctuation. Imported in organize.py 221 lines

cleverRules.py - creates positive and negative annotation files and places each concept sequence into rightful file 90 lines

ruleFcns.py - determines whether the concept sequence is positive or negative for main concept or CUI taking into account polarity, experiencer and time. Imported in cleverRules.py 92 lines
