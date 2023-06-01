{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "786e26cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList = [10, \"a\", \"b\", 3.14]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9f9c27c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 2,
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
   "execution_count": 6,
   "id": "9c499e75",
   "metadata": {},
   "outputs": [],
   "source": [
    "myList[0] = 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c742c65d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[100, 'a', 'b', 3.14]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myList "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c2cd6aac",
   "metadata": {},
   "source": [
    "# Tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a1a11f5f",
   "metadata": {},
   "outputs": [],
   "source": [
    "myTuple = (10, \"a\", \"b\", 3.14)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "3abb4300",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "tuple"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(myTuple) #Immutability"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "dfd350b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myTuple[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f82adb93",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myTuple.index(\"a\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "475da3e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myTuple.count(\"a\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b1fdb100",
   "metadata": {},
   "outputs": [],
   "source": [
    "resultTuple = (10, 100, 20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5717db7c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10, 100, 20)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "resultTuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "5ee26034",
   "metadata": {},
   "outputs": [],
   "source": [
    "resultList = list(resultTuple)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7f28ea87",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 100, 20]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "resultList"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6972e25f",
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
