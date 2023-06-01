{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "eb892d94",
   "metadata": {},
   "source": [
    "# Polymorphism"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c4d9bf34",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Banana():\n",
    "    \n",
    "    def __init__(self, name):\n",
    "        self.name = name\n",
    "        \n",
    "    def info(self):\n",
    "        return f\"100 calories {self.name}\"\n",
    "    \n",
    "class Apple():\n",
    "    \n",
    "    def __init__(self, name):\n",
    "        self.name = name\n",
    "        \n",
    "    def info(self):\n",
    "        return f\"150 calories {self.name}\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9c234a62",
   "metadata": {},
   "outputs": [],
   "source": [
    "banana = Banana(\"banana\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7f47ad89",
   "metadata": {},
   "outputs": [],
   "source": [
    "apple = Apple(\"Apple\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d20ed7c8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'100 calories banana'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "banana.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "64e73200",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'150 calories Apple'"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "apple.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7d08383b",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruitList = [banana, apple]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ac855861",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100 calories banana\n",
      "150 calories Apple\n"
     ]
    }
   ],
   "source": [
    "for fruit in fruitList:\n",
    "    print(fruit.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71798cba",
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
