#!/bin/python3

import xml.etree.ElementTree as ET

data = '''
<person>
    <name>1</name>
    <name>1</name>
    <name>2</name>

    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>
'''

tree = ET.fromstring(data)
names = tree.findall(".//name")
for name in names:
    print(name.text)
print("Name:", tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

data =\
    '''
    <commentinfo>
    <note>This file contains the actual data for your assignment - good luck!</note>
    <comments>
    <comment>
    <name>Mhyren</name>
    <count>99</count>
    </comment>
    <comment>
    <name>Mirrin</name>
    <count>89</count>
    </comment>
    <comment>
    <name>Kerris</name>
    <count>88</count>
    </comment>
    <comment>
    <name>Chin</name>
    <count>87</count>
    </comment>
    <comment>
    <name>Noelani</name>
    <count>84</count>
    </comment>
    <comment>
    <name>Aleisha</name>
    <count>81</count>
    </comment>
    <comment>
    <name>Shakeira</name>
    <count>77</count>
    </comment>
    <comment>
    <name>I</name>
    <count>75</count>
    </comment>
    <comment>
    <name>Donnie</name>
    <count>72</count>
    </comment>
    <comment>
    <name>Virginie</name>
    <count>71</count>
    </comment>
    <comment>
    <name>Farrah</name>
    <count>70</count>
    </comment>
    <comment>
    <name>Cal</name>
    <count>69</count>
    </comment>
    <comment>
    <name>Robyn</name>
    <count>66</count>
    </comment>
    <comment>
    <name>Butali</name>
    <count>66</count>
    </comment>
    <comment>
    <name>Carra</name>
    <count>61</count>
    </comment>
    <comment>
    <name>Keatin</name>
    <count>61</count>
    </comment>
    <comment>
    <name>Becky</name>
    <count>58</count>
    </comment>
    <comment>
    <name>Enya</name>
    <count>57</count>
    </comment>
    <comment>
    <name>Temitayo</name>
    <count>55</count>
    </comment>
    <comment>
    <name>Carley</name>
    <count>55</count>
    </comment>
    <comment>
    <name>Alice</name>
    <count>51</count>
    </comment>
    <comment>
    <name>Lekiesha</name>
    <count>49</count>
    </comment>
    <comment>
    <name>Calli</name>
    <count>48</count>
    </comment>
    <comment>
    <name>Wai</name>
    <count>48</count>
    </comment>
    <comment>
    <name>Paulina</name>
    <count>46</count>
    </comment>
    <comment>
    <name>Brandonlee</name>
    <count>45</count>
    </comment>
    <comment>
    <name>Ammara</name>
    <count>45</count>
    </comment>
    <comment>
    <name>Sylvia</name>
    <count>43</count>
    </comment>
    <comment>
    <name>Ammar</name>
    <count>41</count>
    </comment>
    <comment>
    <name>Ogheneruno</name>
    <count>38</count>
    </comment>
    <comment>
    <name>Renee</name>
    <count>38</count>
    </comment>
    <comment>
    <name>Honeyjac</name>
    <count>34</count>
    </comment>
    <comment>
    <name>Savannah</name>
    <count>33</count>
    </comment>
    <comment>
    <name>Malcolm</name>
    <count>31</count>
    </comment>
    <comment>
    <name>Fenella</name>
    <count>30</count>
    </comment>
    <comment>
    <name>Samarjit</name>
    <count>26</count>
    </comment>
    <comment>
    <name>Haniya</name>
    <count>24</count>
    </comment>
    <comment>
    <name>Kaison</name>
    <count>22</count>
    </comment>
    <comment>
    <name>Qi</name>
    <count>22</count>
    </comment>
    <comment>
    <name>Tasnim</name>
    <count>21</count>
    </comment>
    <comment>
    <name>Marcelina</name>
    <count>18</count>
    </comment>
    <comment>
    <name>Nicki</name>
    <count>14</count>
    </comment>
    <comment>
    <name>Deelan</name>
    <count>9</count>
    </comment>
    <comment>
    <name>Rhiana</name>
    <count>8</count>
    </comment>
    <comment>
    <name>Aman</name>
    <count>6</count>
    </comment>
    <comment>
    <name>Makenzie</name>
    <count>5</count>
    </comment>
    <comment>
    <name>Benjamin</name>
    <count>5</count>
    </comment>
    <comment>
    <name>Magdalene</name>
    <count>4</count>
    </comment>
    <comment>
    <name>Geordie</name>
    <count>1</count>
    </comment>
    <comment>
    <name>Jomuel</name>
    <count>1</count>
    </comment>
    </comments>
    </commentinfo>
    '''

tree = ET.fromstring(data)
print("Retrieved", len(data), "characters")

counts = tree.findall(".//count")
inc = 0
totalSum = 0
for count in counts:
    totalSum += int(count.text)
    inc += 1

print("Count:", inc)
print("Sum:", totalSum)
# print("Count:", len(counts))

