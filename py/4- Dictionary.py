{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "22fa370d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Key - Value Pairing "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2ed5e099",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruits = [\"banana\", \"apple\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "68d5aa7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "calories = [100, 150]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fbadaf15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'banana'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fruits[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8c47ba0e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "calories[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e1e556f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "fitnessDictionary = {\"banana\": 100,\n",
    "                     \"apple\": 150}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b71c0ac7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(fitnessDictionary)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "bd4f90d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dictionary key value olduğu için index yoktur."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "9d092250",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "100"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fitnessDictionary[\"banana\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "46ebf100",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "150"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fitnessDictionary[\"apple\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "903c7bd1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['banana', 'apple'])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fitnessDictionary.keys() #Sadece anahtarları verir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "b0f0a448",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values([100, 150])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fitnessDictionary.values() #Sadece değerleri verir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "23eead89",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 150]"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(fitnessDictionary.values())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "245b580d",
   "metadata": {},
   "outputs": [],
   "source": [
    "fitnessDictionary[\"banana\"] = 200"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "2be20660",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'banana': 200, 'apple': 150}"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fitnessDictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "fccdb51a",
   "metadata": {},
   "outputs": [],
   "source": [
    "fitnessDictionary[\"melon\"] = 300"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "475f22cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'banana': 200, 'apple': 150, 'melon': 300}"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fitnessDictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "66e32195",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "150"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fitnessDictionary.get(\"apple\", 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "e69df959",
   "metadata": {},
   "outputs": [],
   "source": [
    "myDictionary = {100: \"a\", 200: \"b\", 300: \"c\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "152e73a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'a'"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myDictionary[100]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "e842ed11",
   "metadata": {},
   "outputs": [],
   "source": [
    "myDictionary = {\"key1\": \"value1\", \"key2\": \"value2\", \"key3\": \"value3\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "b8b6d87d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'value1'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myDictionary[\"key1\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "0a7d6d28",
   "metadata": {},
   "outputs": [],
   "source": [
    "myMixedDictionary = {\"key1\": 100, \"key2\": 3.14, \"key3\": [10, 20, 30]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "972c2f8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 20, 30]"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myMixedDictionary[\"key3\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "f9315b12",
   "metadata": {},
   "outputs": [],
   "source": [
    "lastDictionary = {\"k1\": 10, \"k2\": [10, 20, 30, 40, 50], \"k3\": \"string\", \"k4\": {\"a\": 100, \"b\": 200}}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "253a960d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lastDictionary[\"k2\"][2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "8cd8ae45",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lastDictionary[\"k4\"][\"b\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e75d08ec",
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
