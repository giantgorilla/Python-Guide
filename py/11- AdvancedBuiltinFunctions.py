{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1b5834b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [10, 20, 30, 40, 50, 60, 70]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2de58236",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.0\n",
      "10.0\n",
      "15.0\n",
      "20.0\n",
      "25.0\n",
      "30.0\n",
      "35.0\n"
     ]
    }
   ],
   "source": [
    "for num in myList:\n",
    "    print(num / 2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "208ae36d",
   "metadata": {},
   "source": [
    "# Range"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "86058ea6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "range(0, 50)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "range(50)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "41335b23",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1298290f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n",
      "22\n",
      "24\n",
      "26\n",
      "28\n",
      "30\n",
      "32\n",
      "34\n",
      "36\n",
      "38\n"
     ]
    }
   ],
   "source": [
    "for num in list (range(20)):\n",
    "    print(num * 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "9cc1a620",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(5, 25))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ac10f88e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 7, 9, 11, 13, 15, 17, 19, 21, 23]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(5, 25, 2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d5910759",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [20, 30, 40, 50, 60]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a55dda3b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "for index in range(len(myList)):\n",
    "    print(index)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58a9cf28",
   "metadata": {},
   "source": [
    "# Enumerate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2024d464",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(0, 20)\n",
      "(1, 30)\n",
      "(2, 40)\n",
      "(3, 50)\n",
      "(4, 60)\n"
     ]
    }
   ],
   "source": [
    "for element in enumerate(myList):\n",
    "    print(element)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f73703ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n",
      "30\n",
      "40\n",
      "50\n",
      "60\n"
     ]
    }
   ],
   "source": [
    "for (index, value) in enumerate(myList):\n",
    "    print(value)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7da97792",
   "metadata": {},
   "source": [
    "# Random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "140d79de",
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import randint"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "6dde6d8b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "41"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "randint(0, 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "50e1a8e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "61"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "randint(0, 100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3665c3ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "from random import shuffle #Shuffle = Karıştırmak"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "a4a61ac1",
   "metadata": {},
   "outputs": [],
   "source": [
    "shuffle(myList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "e17cd855",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[40, 60, 20, 50, 30]"
      ]
     },
     "execution_count": 21,
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
   "execution_count": 22,
   "id": "e9dbf966",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [10, 20, 30, 40, 50, 60, 70]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "36d277ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "randint(0, len(myList))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "c5d46866",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myList[randint(0, len(myList))]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c96d20c8",
   "metadata": {},
   "source": [
    "# Zip"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "a32c0684",
   "metadata": {},
   "outputs": [],
   "source": [
    "foodList = [\"apple\", \"banana\", \"melon\"]\n",
    "caloriesList = [100, 150, 200]\n",
    "dayList = [\"monday\", \"tuesday\", \"wednesday\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "17828ae5",
   "metadata": {},
   "outputs": [],
   "source": [
    "zippedList = list(zip(foodList, caloriesList, dayList))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "869bc60f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('apple', 100, 'monday'),\n",
       " ('banana', 150, 'tuesday'),\n",
       " ('melon', 200, 'wednesday')]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "zippedList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "2dc35aed",
   "metadata": {},
   "outputs": [],
   "source": [
    "newList = []\n",
    "myString = \"Metallica\"\n",
    "\n",
    "for element in myString:\n",
    "    newList.append(element)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "a430a6b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['M', 'e', 't', 'a', 'l', 'l', 'i', 'c', 'a']"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newList"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6a9f6919",
   "metadata": {},
   "source": [
    "# List Comprehension"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "215618eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "newList = [element for element in myString]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "b1532bc1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['M', 'e', 't', 'a', 'l', 'l', 'i', 'c', 'a']"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "398eb6cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "numberList = [10, 20, 30, 40, 50, 60]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "522aaa25",
   "metadata": {},
   "outputs": [],
   "source": [
    "newNumberList = [num for num in numberList]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "076cad91",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 20, 30, 40, 50, 60]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "newNumberList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56aa601b",
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
