{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4a91872b",
   "metadata": {},
   "outputs": [],
   "source": [
    "myString = (\"Hello Python\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "17745939",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Hello', 'Python']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myString.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a10c0aa5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(myString.split())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5053a948",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Immutable - Immutability"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3898b2ba",
   "metadata": {},
   "source": [
    "# List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9e0ab45d",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [10, 20, 30]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "20b972e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(myList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "10f3f7f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 10 \n",
    "y = 20 \n",
    "z = 30"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "471a36d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [x, y, z]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "738c5a7a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 20, 30]"
      ]
     },
     "execution_count": 14,
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
   "execution_count": 15,
   "id": "0d9a36d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [10, 20, 30, 40, 50, 60, 70]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "304db014",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myList[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "96e8b879",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(myList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "37ca9b38",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(myList[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6e759879",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList[0] = 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ef634c20",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 20, 30, 40, 50, 60, 70]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myList #Mutable - Mutability"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "34de19e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 21,
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
   "execution_count": 22,
   "id": "35f1a4e3",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList.append(80) #Append = Listeye veri eklemek için kullanılır."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "04a5377d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 20, 30, 40, 50, 60, 70, 80]"
      ]
     },
     "execution_count": 23,
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
   "execution_count": 24,
   "id": "60d7a142",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myList.count(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "dcd20ba8",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList2 = [15, 25, 35, 45, 55, 65, 75]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "075a8c50",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList.extend(myList2) #Extend = İki listeyi birleştirmek için kullanılır."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "7d9ebfcf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 20, 30, 40, 50, 60, 70, 80, 15, 25, 35, 45, 55, 65, 75]"
      ]
     },
     "execution_count": 27,
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
   "execution_count": 28,
   "id": "fa16b6e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList.insert(10, 4) #10.indexe 4 değerini yerleştirir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "95862edb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 20, 30, 40, 50, 60, 70, 80, 15, 25, 4, 35, 45, 55, 65, 75]"
      ]
     },
     "execution_count": 29,
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
   "execution_count": 30,
   "id": "88c96905",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\nAppend ve Insert arasındaki fark: Append özelliğiyle birlikte eklemek istenilen\\ndeğer listenin sonuna eklenirken Insert özelliğiyle ilk parametre index değeri\\nni, ikinci parametre ise belirtilen indexe hangi değerin ekleneceği yazılır.\\n'"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "Append ve Insert arasındaki fark: Append özelliğiyle birlikte eklemek istenilen\n",
    "değer listenin sonuna eklenirken Insert özelliğiyle ilk parametre index değeri\n",
    "ni, ikinci parametre ise belirtilen indexe hangi değerin ekleneceği yazılır.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "80bd0f53",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "75"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myList.pop() #Pop = Son elemanı listeden çıkartır."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "28174c67",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 20, 30, 40, 50, 60, 70, 80, 15, 25, 4, 35, 45, 55, 65]"
      ]
     },
     "execution_count": 32,
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
   "execution_count": 33,
   "id": "c743106f",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList.remove(4) #Remove = Belirtilen değeri listeden siler."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "2a667e05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 20, 30, 40, 50, 60, 70, 80, 15, 25, 35, 45, 55, 65]"
      ]
     },
     "execution_count": 34,
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
   "execution_count": 35,
   "id": "7b1c48da",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList.reverse() #Reverse = Listeyi tersine çevirir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "35d3fe2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[65, 55, 45, 35, 25, 15, 80, 70, 60, 50, 40, 30, 20, 100]"
      ]
     },
     "execution_count": 36,
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
   "execution_count": 37,
   "id": "0b6ced77",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList.sort() #A'dan Z'ye ya da küçükten büyüğe sıralar."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "f9ea3e55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 100]"
      ]
     },
     "execution_count": 38,
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
   "execution_count": 41,
   "id": "f5bec20f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter X:10\n"
     ]
    }
   ],
   "source": [
    "x = input(\"Enter X:\") #Inputtan gelen her bilgi string olarak algılanır."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "209eaa74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Y:12\n"
     ]
    }
   ],
   "source": [
    "y = input(\"Enter Y:\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "b949fb53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Z:25\n"
     ]
    }
   ],
   "source": [
    "z = input(\"Enter Z:\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "814faf6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "inputList = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "7e267c98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inputList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "3c618e10",
   "metadata": {},
   "outputs": [],
   "source": [
    "inputList.append(x)\n",
    "inputList.append(y)\n",
    "inputList.append(z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "2053f0bb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['10', '12', '25']"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inputList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "7208aa4a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1212'"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "inputList[1] * 2 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "e1b506b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(inputList[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "f10aaff9",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Değer string olarak tutulduğu için matematiksel işlem gerçekleşmedi."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "c3fdc03b",
   "metadata": {},
   "outputs": [],
   "source": [
    "myInteger = 50"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "7ed2a747",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'50'"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str(myInteger)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "424e5c5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "myString = \"40\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "757dd734",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "40"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(myString)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "bd84d79d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int(inputList[1]) * 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "4e9134c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "mixedList = [\"Doğukan\", 100, 3.14]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "ae1d1fa3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "list"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(mixedList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "f9b0538d",
   "metadata": {},
   "outputs": [],
   "source": [
    "list1 = [10, 20, 30]\n",
    "list2 = [40, 50, 60]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "089beab9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 20, 30, 40, 50, 60]"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1 + list2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "14b4d255",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 20, 30, 10, 20, 30]"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1 * 2 #List1'i 2 kez yazdırır."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d20db7a7",
   "metadata": {},
   "source": [
    "# Nested List - İç İçe Liste"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "a2a95be7",
   "metadata": {},
   "outputs": [],
   "source": [
    "myNestedList = [10, 20, 3.14, \"Doğukan\", [1, 2, 3]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "100f83e2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myNestedList[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "60f36ecf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myNestedList[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "2738f973",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.14"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myNestedList[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "e18688a3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Doğukan'"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myNestedList[3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "134e3b33",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3]"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myNestedList[4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "07afaf4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = myNestedList[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "8c6f29d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "6a41c848",
   "metadata": {},
   "outputs": [],
   "source": [
    "list2 = myNestedList[4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "389aff59",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3]"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "4f152f15",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 20, 3.14, 'Doğukan', [1, 2, 3]]"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myNestedList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "90133d8e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3]"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list2 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "951d3b3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myNestedList[4][1] #4.indexte olan iç içe listenin 1. indexini verir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "d65d5584",
   "metadata": {},
   "outputs": [],
   "source": [
    "lastList = [\"a\", \"b\", [\"c\", \"d\", \"e\"], \"f\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "6db15c7c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(lastList)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "cb655611",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'d'"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lastList[2][1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "321573c6",
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
