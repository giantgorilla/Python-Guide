{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "90329614",
   "metadata": {},
   "outputs": [],
   "source": [
    "#for loop, while loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a282f324",
   "metadata": {},
   "outputs": [],
   "source": [
    "#for loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "6bfbe570",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [10, 20, 30, 40, 50, 60, 70]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7df81fca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.0"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myList[0] / 5 * 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ee9e0556",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.0\n",
      "8.0\n",
      "12.0\n",
      "16.0\n",
      "20.0\n",
      "24.0\n",
      "28.0\n"
     ]
    }
   ],
   "source": [
    "for number in myList:\n",
    "    print(number / 5 * 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0c3c542e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "For Loop Started\n",
      "4.0\n",
      "8.0\n",
      "12.0\n",
      "16.0\n",
      "20.0\n",
      "24.0\n",
      "28.0\n",
      "For Loop Ended\n"
     ]
    }
   ],
   "source": [
    "print(\"For Loop Started\")\n",
    "for x in myList:\n",
    "    new_number = x / 5 * 2\n",
    "    print(new_number)\n",
    "print(\"For Loop Ended\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "a594be33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number does not divide without a remainder..\n",
      "The number does not divide without a remainder..\n",
      "The number is divided without a remainder..\n",
      "The number does not divide without a remainder..\n",
      "The number does not divide without a remainder..\n",
      "The number is divided without a remainder..\n",
      "The number does not divide without a remainder..\n"
     ]
    }
   ],
   "source": [
    "for number in myList:\n",
    "    if number %6 == 0:\n",
    "        print(\"The number is divided without a remainder..\")\n",
    "    else:\n",
    "        print(\"The number does not divide without a remainder..\")\n",
    "        \n",
    "        #Yazılı Printout"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6889fbc5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "60\n"
     ]
    }
   ],
   "source": [
    "for number in myList:\n",
    "    if number %6 == 0:\n",
    "        print(number)\n",
    "        \n",
    "        #Sayılı Printout"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "63c275fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "17affb15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Odd Number\n",
      "Even Number\n",
      "Odd Number\n",
      "Even Number\n",
      "Odd Number\n",
      "Even Number\n",
      "Odd Number\n",
      "Even Number\n",
      "Odd Number\n",
      "Even Number\n"
     ]
    }
   ],
   "source": [
    "for number in numberList:\n",
    "    if number %2 == 0:\n",
    "        print(\"Even Number\")\n",
    "    else:\n",
    "        print(\"Odd Number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "19869155",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "for number in numberList:\n",
    "    if number %2 == 0:\n",
    "        print(number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a8dbc94b",
   "metadata": {},
   "outputs": [],
   "source": [
    "myTuple = (10, 20, 30, 40, 50, 60, 70)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "b42175a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.0\n",
      "8.0\n",
      "12.0\n",
      "16.0\n",
      "20.0\n",
      "24.0\n",
      "28.0\n"
     ]
    }
   ],
   "source": [
    "for number in myTuple:\n",
    "    print(number / 5 * 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "1a00b0a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "myNewList = [(\"a\", \"b\"), (\"c\", \"d\"), (\"e\", \"f\"), (\"g\", \"h\")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "0c4aed0d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(myNewList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "6d3cf332",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('a', 'b')"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myNewList[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "5b3f83fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('a', 'b')\n",
      "('c', 'd')\n",
      "('e', 'f')\n",
      "('g', 'h')\n"
     ]
    }
   ],
   "source": [
    "for element in myNewList:\n",
    "    print(element)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "a1043a8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Tuple Unpacking"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "caf0fb0b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n",
      "c\n",
      "e\n",
      "g\n"
     ]
    }
   ],
   "source": [
    "for (x, y) in myNewList:\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "8115d87f",
   "metadata": {},
   "outputs": [],
   "source": [
    "myTupleList = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "b77b1e3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(myTupleList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "1516a331",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 1\n",
      "3 4\n",
      "6 7\n",
      "9 10\n"
     ]
    }
   ],
   "source": [
    "for (x, y, z) in myTupleList:\n",
    "    print(x, y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "2155eb09",
   "metadata": {},
   "outputs": [],
   "source": [
    "mySet = {1, 2, 3, 4, 5}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "2db3b7da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3, 4, 5}"
      ]
     },
     "execution_count": 43,
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
   "execution_count": 44,
   "id": "8bde60e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(mySet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "05fa3ca8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for number in mySet:\n",
    "    print(number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "01a750e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "myDictionary = {\"k1\": 100, \"k2\": 200, \"k3\": 300}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "a4883191",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "k1\n",
      "k2\n",
      "k3\n"
     ]
    }
   ],
   "source": [
    "for element in myDictionary:\n",
    "    print(element)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "1076d705",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([('k1', 100), ('k2', 200), ('k3', 300)])"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myDictionary.items()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "197101aa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "200\n",
      "300\n"
     ]
    }
   ],
   "source": [
    "for (key, value) in myDictionary.items():\n",
    "    print(value)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1abc0d6c",
   "metadata": {},
   "source": [
    "# Continue - Break - Pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "56de2d83",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [10, 20, 30, 40, 50, 60, 70]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "cf7652c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "For Loop Started\n",
      "10\n",
      "20\n",
      "30\n",
      "40\n",
      "50\n",
      "60\n",
      "70\n",
      "For Loop Ended\n"
     ]
    }
   ],
   "source": [
    "print(\"For Loop Started\")\n",
    "for number in myList:\n",
    "    print(number)\n",
    "print(\"For Loop Ended\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "2c51b17e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n",
      "30\n",
      "40\n",
      "Yes!\n"
     ]
    }
   ],
   "source": [
    "#40'ı bulunca duran kod bloğunu yazınız.\n",
    "\n",
    "for number in myList:\n",
    "    print(number)\n",
    "    if number == 40:\n",
    "        print(\"Yes!\")\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "fdea4801",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n",
      "30\n",
      "40\n",
      "Yes!\n",
      "50\n",
      "60\n",
      "70\n"
     ]
    }
   ],
   "source": [
    "for number in myList:\n",
    "    print(number)\n",
    "    if number == 40:\n",
    "        print(\"Yes!\")\n",
    "        continue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "a84dc455",
   "metadata": {},
   "outputs": [],
   "source": [
    "for number in myList:\n",
    "    pass"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19a1cb1c",
   "metadata": {},
   "source": [
    "# While "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "30ba6fb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bde9c2f8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "While Loop Started\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "While Loop Ended\n"
     ]
    }
   ],
   "source": [
    "print(\"While Loop Started\")\n",
    "while x < 10:\n",
    "    print(x)\n",
    "    \n",
    "    x = x + 1\n",
    "    \n",
    "print(\"While Loop Ended\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "41793cc2",
   "metadata": {},
   "outputs": [],
   "source": [
    "lastList = [10, 20, 30, 40, 50]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "78b464bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20 in lastList\n",
      "20 in lastList\n",
      "20 in lastList\n",
      "20 in lastList\n"
     ]
    }
   ],
   "source": [
    "while 20 in lastList:\n",
    "    print(\"20 in lastList\")\n",
    "    lastList.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5c074340",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Value Of P: 0\n",
      "Value Of P: 1\n",
      "Value Of P: 2\n",
      "Value Of P: 3\n",
      "Value Of P: 4\n",
      "Value Of P: 5\n",
      "Value Of P: 6\n",
      "Value Of P: 7\n",
      "Value Of P: 8\n",
      "Value Of P: 9\n",
      "Value Of P: 10\n",
      "Value Of P: 11\n",
      "Value Of P: 12\n",
      "Value Of P: 13\n",
      "Value Of P: 14\n",
      "Value Of P: 15\n",
      "Value Of P: 16\n",
      "Value Of P: 17\n",
      "Value Of P: 18\n",
      "Value Of P: 19\n"
     ]
    }
   ],
   "source": [
    "p = 0\n",
    "while p < 20:\n",
    "    print(f\"Value Of P: {p}\")\n",
    "    \n",
    "    p += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "472456a5",
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
