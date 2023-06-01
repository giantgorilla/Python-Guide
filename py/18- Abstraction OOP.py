{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "5562e6c5",
   "metadata": {},
   "source": [
    "# Abstraction - Soyutlama"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c118696f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from abc import ABC, abstractmethod"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5049b387",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Car(ABC):\n",
    "    \n",
    "    @abstractmethod\n",
    "    def maxSpeed(self):\n",
    "        pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1a34f7cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#myCar = Car()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "68c3b46f",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Tesla(Car):\n",
    "    \n",
    "    def maxSpeed(self):\n",
    "        print(\"200 KM/H\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "c90312ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "tesla = Tesla()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "bbcc5811",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "200 KM/H\n"
     ]
    }
   ],
   "source": [
    "tesla.maxSpeed()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "0d665551",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Mercedes(Car):\n",
    "    \n",
    "    def maxSpeed(self):\n",
    "        print(\"250 KM/H\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "8e6200ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "mercedes = Mercedes()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "22b56cc9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "250 KM/H\n"
     ]
    }
   ],
   "source": [
    "mercedes.maxSpeed()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb0978e6",
   "metadata": {},
   "source": [
    "# Özel Methodlar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "b1b24ae8",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Fruit():\n",
    "    \n",
    "    def __init__(self, name, calories):\n",
    "        self.name =  name\n",
    "        self.calories = calories\n",
    "    \n",
    "    def __str__(self):\n",
    "        return f\"{self.name}: {self.calories} calories\"\n",
    "    \n",
    "    def __len__(self):\n",
    "        return self.calories"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "5b05eb62",
   "metadata": {},
   "outputs": [],
   "source": [
    "myFruit = Fruit(\"Banana\", 150)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "be18065e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "150"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myFruit.calories"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "8bc764a2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Banana'"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myFruit.name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "d9351c18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Banana: 150 calories\n"
     ]
    }
   ],
   "source": [
    "print(myFruit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "be8ee68f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "150"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(myFruit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "6326231e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#https://www.informit.com/articles/article.aspx?p=453682&seqNum=6 - Özel Method"
   ]
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
