{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e3ac624e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Unique Elements, Unordered - Her bir elemandan 1 tane olabilir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f417cd64",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [10, 20, 30, 10, 20, 40, 10, 20, 40]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9ae0c195",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(myList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "644dd87f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 20, 30, 10, 20, 40, 10, 20, 40]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "120e6968",
   "metadata": {},
   "outputs": [],
   "source": [
    "mySet = set(myList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f942609e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 30, 40}"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mySet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "7c5b2ba6",
   "metadata": {},
   "outputs": [],
   "source": [
    "mySet = {10, 20, 30, 10, 20, 40, 10, 20, 40}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "28498fa1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 30, 40}"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mySet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3d083ed0",
   "metadata": {},
   "outputs": [],
   "source": [
    "mySet.add(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "17b9f8e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 30, 40}"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mySet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "603d53d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "mySet.add(50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3f2d2d9d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 30, 40, 50}"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mySet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "11d2ec04",
   "metadata": {},
   "outputs": [],
   "source": [
    "mySet2 = {30, 40, 50, 60, 70}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a0ba480a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 30, 40, 50}"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mySet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "3985d679",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{30, 40, 50, 60, 70}"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mySet2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "72ca49fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 30, 40, 50, 60, 70}"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mySet.union(mySet2) #Union = Birleştirmek için kullanılır."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "6e1abdd8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{30, 40, 50}"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mySet.intersection(mySet2) #Intersection = Kesişim için kullanılır."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "3920e142",
   "metadata": {},
   "outputs": [],
   "source": [
    "countryList = [\"de\", \"fr\", \"tr\", \"fr\", \"tr\", \"tr\", \"de\", \"nl\", \"de\", \"tr\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "845c5923",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(set(countryList))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b24a5556",
   "metadata": {},
   "outputs": [],
   "source": [
    "emptySet = set()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "e653f0cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "set"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(emptySet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "d72a2cbd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(emptySet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "3bab8989",
   "metadata": {},
   "outputs": [],
   "source": [
    "emptySet.add(10)\n",
    "emptySet.add(10)\n",
    "emptySet.add(10)\n",
    "emptySet.add(20)\n",
    "emptySet.add(30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "bd47d715",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{10, 20, 30}"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emptySet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "e9b60eb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "emptyList = list()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "3c3a7f5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "emptyList.append(10)\n",
    "emptyList.append(20)\n",
    "emptyList.append(30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "086e8c85",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 20, 30]"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emptyList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "fd6b40a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "emptyDictionary = dict()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "744328a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "emptyDictionary[\"a\"] = 10\n",
    "emptyDictionary[\"b\"] = 20"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "6f29aca1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'a': 10, 'b': 20}"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emptyDictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61fea133",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
