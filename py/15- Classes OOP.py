{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dd76b2c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "dogukanName = \"Doğukan\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "3de5cd81",
   "metadata": {},
   "outputs": [],
   "source": [
    "dogukanAge = 21"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "44ffa8eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "dogukanGender = \"Male\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3cae2c8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "atlasName = \"Atlas\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c4097bcf",
   "metadata": {},
   "outputs": [],
   "source": [
    "atlasAge = 14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8a384afa",
   "metadata": {},
   "outputs": [],
   "source": [
    "atlasGender = \"Male\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "820215c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Person():\n",
    "    #Property\n",
    "    #name = \"\"\n",
    "    #age = 0\n",
    "    #gender = \"\"\n",
    "    \n",
    "    #Initializer Method  \n",
    "    def __init__(self, name, age, gender): #Initializer\n",
    "        self.name = name\n",
    "        self.age = age\n",
    "        self.gender = gender\n",
    "        \n",
    "    #method\n",
    "    def printName(self):\n",
    "        print(self.name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "9f370b25",
   "metadata": {},
   "outputs": [],
   "source": [
    "dogukan = Person(\"Doğukan\", 21, \"Male\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "25df8f5b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "__main__.Person"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(dogukan)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "38b08e9c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Doğukan'"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dogukan.name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "45c2e64e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "21"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dogukan.age"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "5f69e910",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Male'"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dogukan.gender"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "edea1808",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Doğukan\n"
     ]
    }
   ],
   "source": [
    " dogukan.printName()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "86267e7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Dog():\n",
    "    \n",
    "    year = 7\n",
    "    \n",
    "    def __init__(self, age):\n",
    "    \tself.age = age\n",
    "        \n",
    "    def humanAge(self):\n",
    "        return self.age * self.year #Dog.year -> self.year   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "7a5b24b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "myDog = Dog(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "f45e21b3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myDog.age"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "301bd1b3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "21"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myDog.humanAge()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "251062ff",
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
