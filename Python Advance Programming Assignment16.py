#!/usr/bin/env python
# coding: utf-8

# 1. Rondo Form is a type of musical structure, in which there is a recurring
# theme/refrain, notated as A. Here are the rules for valid rondo forms:
# - Rondo forms always start and end with an A section.
# - In between the A sections, there should be contrasting sections notated as
# B, then C, then D, etc... No letter should be skipped.
# - There shouldn&#39;t be any repeats in the sequence (such as ABBACCA).
# Create a function which validates whether a given string is a valid Rondo
# Form.
# Examples
# valid_rondo(&quot;ABACADAEAFAGAHAIAJA&quot;) ➞ True
# valid_rondo(&quot;ABA&quot;) ➞ True
# valid_rondo(&quot;ABBACCA&quot;) ➞ False
# valid_rondo(&quot;ACAC&quot;) ➞ False
# valid_rondo(&quot;A&quot;) ➞ False
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def valid_rondo(in_string):
    in_string_x = in_string.replace('A','')
    in_string_x = list(in_string_x)
    output = False
    if len(in_string_x) == 1:
            output= True
    else:
        for ele in range(len(in_string_x)-1):
            if ord(in_string_x[ele]) < ord(in_string_x[ele+1]):
                output= True
            else:
                output = False
                break
    print(f"valid_rondo({in_string}) ➞ {output}")
   
valid_rondo("ABACADAEAFAGAHAIAJA")
valid_rondo("ABA")
valid_rondo("ABBACCA")
valid_rondo("ACAC")
valid_rondo("A")


# 2. Create a function that returns the whole of the first sentence which
# contains a specific word. Include the full stop at the end of the sentence.
# Examples
# txt = &quot;I have a cat. I have a mat. Things are going swell.&quot;
# sentence_searcher(txt, &quot;have&quot;) ➞ &quot;I have a cat.&quot;
# sentence_searcher(txt, &quot;MAT&quot;) ➞ &quot;I have a mat.&quot;
# sentence_searcher(txt, &quot;things&quot;) ➞ &quot;Things are going swell.&quot;
# sentence_searcher(txt, &quot;flat&quot;) ➞ &quot;&quot;
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


def sentence_searcher(in_string, search_text):
    output = '""'
    for ele in in_string.split(". "):
        if len(ele.lower().replace(search_text.lower(),'')) != len(ele):
            output = ele
            break
    print(f'sentence_searcher{in_string,search_text} ➞ {output}')

txt = "I have a cat. I have a mat. Things are going swell."

sentence_searcher(txt, "have")
sentence_searcher(txt, "MAT")
sentence_searcher(txt, "things")
sentence_searcher(txt, "flat")


# 3. Given a number, find the &quot;round &quot;of each digit of the number. An integer is
# called &quot;round&quot; if all its digits except the leftmost (most significant) are equal to
# zero.
# - Round numbers: 4000, 1, 9, 800, 90
# - Not round numbers: 110, 707, 222, 1001
# 
# Create a function that takes a number and returns the &quot;round&quot; of each digit
# (except if the digit is zero) as a string. Check out the following examples for
# more clarification.
# Examples
# sum_round(101) ➞ &quot;1 100&quot;
# sum_round(1234) ➞ &quot;4 30 200 1000&quot;
# sum_round(54210) ➞ &quot;10 200 4000 50000&quot;
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def sum_round(in_num):
    output = []
    in_num = str(in_num)
    for ele in range(len(in_num)):
        if in_num[ele] != '0':
            output.append(in_num[ele]+len(in_num[ele+1:])*'0')
    print(f'sum_round({in_num}) ➞ {" ".join(output[::-1])}')
        
sum_round(101)
sum_round(1234)
sum_round(54210)


# 4. Your task, is to create N x N multiplication table, of size n provided in
# parameter.
# For example, when n is 5, the multiplication table is:
# - 1, 2, 3, 4, 5
# - 2, 4, 6, 8, 10
# - 3, 6, 9, 12, 15
# - 4, 8, 12, 16, 20
# - 5, 10, 15, 20, 25
# This example will result in:
# [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20,
# 25]]
# Examples
# multiplication_table(1) ➞ [[1]]
# multiplication_table(3) ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def multiplication_table(in_num):
    out_list =[]
    for a in range(1,in_num+1):
        temp_list = []
        for b in range(1,in_num+1):
            temp_list.append(a*b)
        out_list.append(temp_list)
    print(f'multiplication_table({in_num}) ➞ {out_list}')
        
multiplication_table(3) 
multiplication_table(1)
multiplication_table(5)


# 5. Create a function that returns True if two lines rhyme and False otherwise.
# For the purposes of this exercise, two lines rhyme if the last word from each
# sentence contains the same vowels.
# Examples
# does_rhyme(&quot;Sam I am!&quot;, &quot;Green eggs and ham.&quot;) ➞ True
# does_rhyme(&quot;Sam I am!&quot;, &quot;Green eggs and HAM.&quot;) ➞ True
# # Capitalization and punctuation should not matter.
# 
# does_rhyme(&quot;You are off to the races&quot;, &quot;a splendid day.&quot;) ➞ False
# does_rhyme(&quot;and frequently do?&quot;, &quot;you gotta move.&quot;) ➞ False
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def does_rhyme(in_one,in_two):
    vowels = 'aeiou'
    output= False
    in_one_rhyme = [x.lower() for x in in_one.split(" ")[-1] if x.lower() in vowels]
    in_two_rhyme = [x.lower() for x in in_two.split(" ")[-1] if x.lower() in vowels]
    if in_one_rhyme == in_two_rhyme:
        output = True
    print(f'does_rhyme{in_one,in_two} ➞ {output}')
    
does_rhyme("Sam I am!", "Green eggs and ham.")
does_rhyme("Sam I am!", "Green eggs and HAM.")
does_rhyme("You are off to the races", "a splendid day.")
does_rhyme("and frequently do?", "you gotta move.")

