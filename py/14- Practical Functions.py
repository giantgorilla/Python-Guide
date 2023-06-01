{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ca82a6e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def divideNumber(number):\n",
    "    return number / 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "56518105",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7.5"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "divideNumber(15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8fdf286a",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [10, 20, 30, 16, 18, 22, 39, 41, 57, 59]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "63ec2bca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5.0, 10.0, 15.0, 8.0, 9.0, 11.0, 19.5, 20.5, 28.5, 29.5]\n"
     ]
    }
   ],
   "source": [
    "myResultList = []\n",
    "\n",
    "for num in myList:\n",
    "    myResultList.append(divideNumber(num))\n",
    "print(myResultList)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2f33c8fd",
   "metadata": {},
   "source": [
    "# Map Function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a1ca02ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5.0, 10.0, 15.0, 8.0, 9.0, 11.0, 19.5, 20.5, 28.5, 29.5]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(map(divideNumber, myList))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "7b3bdb58",
   "metadata": {},
   "outputs": [],
   "source": [
    "def controlString(string):\n",
    "    return \"Doğukan\" in string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f9b2761c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "controlString(\"Doğukan Bostancı\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "693d9ea6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "controlString(\"Bostancı\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "be0e8686",
   "metadata": {},
   "outputs": [],
   "source": [
    "myStringList = [\"Doğukan\", \"Doğukan Bostancı\", \"Bostancı\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f5212352",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[True, True, False]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(map(controlString, myStringList))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "31a5c1e1",
   "metadata": {},
   "source": [
    "# Filter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f5a02bd9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Doğukan', 'Doğukan Bostancı']"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(filter(controlString, myStringList))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e73216c",
   "metadata": {},
   "source": [
    "# Lambda"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "5c9ae448",
   "metadata": {},
   "outputs": [],
   "source": [
    "multiplyLambda = lambda num : num * 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "984cd64b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "function"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(multiplyLambda)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "9475edc2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "60"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "multiplyLambda(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ef830638",
   "metadata": {},
   "outputs": [],
   "source": [
    "numList = [10, 20, 30, 40, 50]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "dee09b09",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2.5, 5.0, 7.5, 10.0, 12.5]"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(map(lambda num: num /4 ,numList))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6803c4ee",
   "metadata": {},
   "source": [
    "# Scope - Kapsam"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "06d4b731",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 20\n",
    "\n",
    "def multiply(num):\n",
    "    x = 5 \n",
    "    return num * x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "2cc8d763",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\tmultiply(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "70f7e2a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 20\n",
    "\n",
    "def multiply(num):\n",
    "    return num * x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e061869d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "200"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "multiply(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20692e63",
   "metadata": {},
   "source": [
    "# LEGB - L = Local, E = Enclosing, G = Global, B = Built- In"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "2ceec80e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Global\n",
    "myString = \"Doğukan\"\n",
    "\n",
    "def myFunction():\n",
    "    #Enclosing\n",
    "    myString = \"Doğukan 2\"\n",
    "    print(myString)\n",
    "    \n",
    "    def myFunction2():\n",
    "        #Local\n",
    "        myString = \"Doğukan 3\"\n",
    "        print(myString)\n",
    "        \n",
    "    myFunction2()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "61ff0041",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Doğukan'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myString"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "01be8c27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Doğukan 2\n",
      "Doğukan 3\n"
     ]
    }
   ],
   "source": [
    "myFunction()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "3bcb5f49",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Doğukan'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myString"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c4a14dd5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def test1():\n",
    "    myVariable = 10\n",
    "    print(myVariable * 2)\n",
    "    \n",
    "def test2():\n",
    "    print(myVariable * 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5ef58640",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "test1()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "75b57ddd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#test2()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "cdcf453d",
   "metadata": {},
   "outputs": [],
   "source": [
    "y = 10\n",
    "\n",
    "def changeY():\n",
    "    global y\n",
    "    y = 5\n",
    "    print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "f2d2d9b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "changeY()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "0283b23c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a2ecdb7",
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
