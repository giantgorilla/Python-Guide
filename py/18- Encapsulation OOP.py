{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fbab8e99",
   "metadata": {},
   "source": [
    "# Encapsulation - Kapsülleme"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "67ec8119",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Phone():\n",
    "    \n",
    "    def __init__(self, name, price):\n",
    "        self.name = name\n",
    "        self.__price = price #.__ ile kapsülleme yapılır.\n",
    "        \n",
    "    def info(self):\n",
    "        print(f\"{self.name} price is: {self.__price}\")\n",
    "        \n",
    "    def changePrice(self, price):\n",
    "        self.__price = price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7a8fdccb",
   "metadata": {},
   "outputs": [],
   "source": [
    "iphone = Phone(\"iPhone 14\", 500)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4d5f2b6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iPhone 14 price is: 500\n"
     ]
    }
   ],
   "source": [
    "iphone.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "49b79ff4",
   "metadata": {},
   "outputs": [],
   "source": [
    "iphone.price = 400"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5a80be5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iPhone 14 price is: 500\n"
     ]
    }
   ],
   "source": [
    "iphone.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "025e242f",
   "metadata": {},
   "outputs": [],
   "source": [
    "iphone.changePrice(300)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c9d2697e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "iPhone 14 price is: 300\n"
     ]
    }
   ],
   "source": [
    "iphone.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a9ddab7",
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
