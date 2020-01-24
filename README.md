# Estimating-Vocabulary
Some scripts to estimate how many English words I know  
  
## About program
This is a Python script to estimate how much vocabulary you know.  You can run it from the command line using command line arguments.  
The script can be used to take a random sample of words from the dictionary and put them into a .txt file.  From here you will need  
to manually edit the .txt file.  Mark each word you know with a 1 and each word you don't know with a 0.  Separate the words from  
their labels using a space.  
  
Once your .txt file is labeled, you can then use it to estimate how many total English words you know.  I'll probably make a front-end for  
this script in React in a few days so you don't need to deal with a .txt file.  But I needed to make it quickly, so there is currently  
no front-end (it's for a class).  
  
The dictionary I am using is from here:  
https://github.com/dwyl/english-words  
  
### Commands:
  
  --help  
  description:  
  prints a description of how to use the program.  This is also the default behavior of the script if you don't use any arguments  
    
  --make <optional sample size argument>  
  description:  
  creates an unlabed sample of words from the dictionary called "sample.txt".  Will not run if this file already exists.  The  
  default sample size is 500, but you can set your own sample as well.  
    
  --estimate <optional argument for delimiter>  
  you should add labels to the sample.txt file before using this.  By default, my script assumes you separate a word and its label
  with a space.  But if you hate that and want to use some other character, you can do that and then give the delimiter you used as
  a command line argument.  Since the input is split based on the delimiter, don't use a delimiter that will be in the words or the
  script won't work right.
    
  --clean  
  If you wanted a more verbose was of typing 'rm sample.txt' then you can use this.  
