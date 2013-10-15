"""
Sort Words
----------

Given a (partial) sentence from a speech, print out
a list of the words in the sentence in alphabetical order.
Also print out just the first two words and the last
two words in the sorted list.

::

    speech = '''Four score and seven years ago our fathers brought forth 
             on this continent a new nation, conceived in Liberty, and 
             dedicated to the proposition that all men are created equal.
             '''


Ignore case and punctuation.

See :ref:`sort-words-solution`.
"""

speech = '''Four score and seven years ago our fathers brought forth 
         on this continent a new nation, conceived in Liberty, and 
         dedicated to the proposition that all men are created equal.
         '''
speech = speech.lower() # convert to lower case
speech = speech.replace('.','') # remove periods
speech = speech.replace(',','') # remove commas

words = speech.split() # convert to list

words.sort() # sort the list

print ' '.join(words) # sorted words
print ' '.join(words[:2]) # first two words
print ' '.join(words[-2:]) # last two words

