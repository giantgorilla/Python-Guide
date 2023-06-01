{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "81a13fda",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 5\n",
    "y = 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eba928d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x > y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3555b776",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x < y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e501e2a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y < x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9c1cf9a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "y = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "bbf5b17c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x >= y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ac906711",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x <= y "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d930573c",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 10 \n",
    "y = 8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "db7d651e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x == y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "60cec49d",
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
    "x != y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e2474866",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\n> = Büyüktür\\n< = Küçüktür\\n>= Büyük Eşittir\\n<= Küçük Eşittir\\n== Eşittir\\n!= Eşit Değildir\\n'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"\n",
    "> = Büyüktür\n",
    "< = Küçüktür\n",
    ">= Büyük Eşittir\n",
    "<= Küçük Eşittir\n",
    "== Eşittir\n",
    "!= Eşit Değildir\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ed1e2fa3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2 > 1 and 3 > 2 #and olduğu için iki koşulunda doğru olması gerekir."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f2177931",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "2 > 1 or 3 < 2 #or olduğu için iki koşulunda doğru olmasına gerek yoktur."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c08cb10c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not 1 == 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "03b0001d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 in [10, 20, 30] #Listenin içerisinde 10 var mı ? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "551a9d65",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 not in [10, 20, 30] #List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "40a10aee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "5 in [10, 20, 30]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "2acc87b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 in {10, 20, 30} #Set"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "23e0873b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "my_dictionary = {\"a\": 10, \"b\": 20, \"c\": 30}\n",
    "10 in my_dictionary.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "0cd17bf9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 in my_dictionary.values() #Dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "ea0ba641",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"b\" in my_dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "dc240d8b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 in (10, 20, 30) #Tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6337e26d",
   "metadata": {},
   "outputs": [],
   "source": [
    "mySuperHero = \"Batman\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "53b02837",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My Super Hero is Batman\n"
     ]
    }
   ],
   "source": [
    "if mySuperHero == \"Batman\":\n",
    "    print(\"My Super Hero is Batman\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "63968a32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Your Super Hero: x\n"
     ]
    }
   ],
   "source": [
    "mySuperHero = input(\"Enter Your Super Hero: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "21139d6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Undefined\n"
     ]
    }
   ],
   "source": [
    "if mySuperHero == \"Superman\":\n",
    "    print(\"Your Super Hero is Superman\")\n",
    "\n",
    "elif mySuperHero == \"Batman\":\n",
    "    print(\"Wrong Super Hero\")\n",
    "    \n",
    "else:\n",
    "    print(\"Undefined\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "5c95acad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Your Age: 22\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"Enter Your Age: \"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "249d00f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You are come of age\n"
     ]
    }
   ],
   "source": [
    "if age > 18:\n",
    "    print(\"You are come of age\")\n",
    "elif age >= 18:\n",
    "    print(\"You are come of age\")\n",
    "else:\n",
    "    print(\"You are underage\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "4ab7dfee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Your Super Hero: Spider Man\n"
     ]
    }
   ],
   "source": [
    "mySuperHero = input(\"Enter Your Super Hero: \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "1a5f1024",
   "metadata": {},
   "outputs": [],
   "source": [
    "mySuperHeroList = [\"Spider Man\", \"Iron Man\", \"Thor\", \"Black Widow\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "454b13c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yes, he/she here!\n"
     ]
    }
   ],
   "source": [
    "if mySuperHero in mySuperHeroList:\n",
    "    print(\"Yes, he/she here!\")\n",
    "else:\n",
    "    print(\"Sorry, he/she not here\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7dc3656",
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
