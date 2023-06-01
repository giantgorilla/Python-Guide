{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1307323c",
   "metadata": {},
   "source": [
    "# Inheritance - Kalıtım"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6c0a46a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Musician():\n",
    "    \n",
    "    def __init__(self, name):\n",
    "        self.name = name\n",
    "        print(\"Musician Class\")\n",
    "        \n",
    "    def test1(self):\n",
    "        print(\"Test 1\")\n",
    "        \n",
    "    def test2(self):\n",
    "        print(\"Test 2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "6eaf244a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Musician Class\n"
     ]
    }
   ],
   "source": [
    "dogukan = Musician(\"Dogukan\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9b38ab5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "class MusicianPlus(Musician):\n",
    "    \n",
    "    def __init__(self, name):\n",
    "        Musician.__init__(self, name)\n",
    "        print(\"Musician Plus\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e78cb96c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Musician Class\n",
      "Musician Plus\n"
     ]
    }
   ],
   "source": [
    "atlas = MusicianPlus(\"Atlas\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5356d294",
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
