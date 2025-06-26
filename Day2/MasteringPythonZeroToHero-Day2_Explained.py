#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Variable


# In[2]:


# Define an integer variable `x` and assign the value 3
x=3
get_ipython().run_line_magic('whos', '')
print(type(x))


# In[3]:


# Reassign `x` with a float value 5.7
x=5.7
get_ipython().run_line_magic('whos', '')
print(type(x))


# In[4]:


# Assign a float value to variable `abc`
abc=556.32
get_ipython().run_line_magic('whos', '')


# In[5]:


# Multiple variable assignments in one line
a,b,c,d,f= 3,5,6.0,7.2,-3
get_ipython().run_line_magic('whos', '')


# In[6]:


# Delete the variable `abc` from memory
del abc


# In[7]:


get_ipython().run_line_magic('whos', '')


# In[8]:


# Define a complex number variable `c`
c=2+4j


# In[9]:


print(type(c))


# In[10]:


# Assign a string value to variable `s`
s="Hello world"
print(type(s))


# In[11]:


# Exponentiation: 2 to the power of 3
x=2**3


# In[12]:


print(x)


# In[13]:


# Division of x by 3
x/3


# In[14]:


#Mod


# In[15]:


# Assign float value to `v`
v=5.5
# Assign integer value to `g`
g=2
# Modulus operation: remainder of v divided by g
p=v%g
print(p)


# In[16]:


#Floor division


# In[17]:


# Assign float value to `v`
v=5.5 
# Assign integer value to `g`
g=2
# Floor division: v divided by g, discarding the remainder
p=v//g
print(p)


# In[18]:


# Add variables a and b and assign to `sumofaAndb`
sumofaAndb=a+b


# In[19]:


print(sumofaAndb)


# In[20]:


# Check type of the result of a+d
type(a+d)


# In[21]:


# Expression with arithmetic and power
v=((a+d)**3)/4


# In[22]:


print(v)


# In[23]:


# Define string `s1`
s1="hello"
# Define string `s2`
s2=" world"
# Concatenate strings s1 and s2
s=s1+s2
print(s)


# In[24]:


# Check if a equals b
a==b


# In[25]:


# Check if a not equals b
a != b


# In[26]:


# Check if a is less than b
a<b


# In[27]:


# bool


# In[28]:


# Assign boolean True to a
a=True
# Assign boolean True to b
b=True
# Assign boolean False to c
c= False
get_ipython().run_line_magic('whos', '')


# In[29]:


# Logical AND of a and b
print(a and b)
# Logical AND of b and c
print(b and c)
# Logical AND of a and c
print(a and c)
# Logical OR of a and c
d= a or c
# Print value of d (False)
print(d)


# In[33]:


# Logical NOT of c
not(c)
print(c)
type(c)


# #compairsions

# In[34]:


# Comparison: 2 is less than 3
print(2<3)


# In[35]:


# Assign result of comparison to variable c
c=2<3
print(type(c))
print(c)


# In[36]:


# Check if 3 equals 4
d=3==4


# In[37]:


# Print value of d (False)
print(d)


# In[38]:


# True: Python treats int and float with same value as equal
3==3.0


# In[39]:


# Assign 4 to x
x=4
# Assign 9 to y
y=9
# Assign 8.3 to z
z=8.3
# Assign -3 to r
r=-3


# In[40]:


(x<y) and (z<y) or (r==x)


# In[41]:


True or False and True
False or True and True
False or False and True
False or False and False


# In[42]:


print((not(2!=3)and True) or (False and True))


# In[43]:


print(round(4.6))


# In[44]:


print(round(4.5584,3))


# In[45]:


# Return tuple (quotient, remainder) of 27/5
divmod(27,5)


# In[48]:


# Store the result of divmod(34,9) in variable G
G=divmod(34,9)


# In[49]:


# Print the tuple G
print(G)


# In[50]:


# Check the type of G (tuple)
type(G)


# In[51]:


# Access second element (remainder) of tuple G
G[1]


# In[ ]:




