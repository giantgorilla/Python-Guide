{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7d306e4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing myfile.txt\n"
     ]
    }
   ],
   "source": [
    "%%writefile myfile.txt\n",
    "test 1\n",
    "test 2\n",
    "test 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5a250115",
   "metadata": {},
   "outputs": [],
   "source": [
    "myFile = open(\"myfile.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b090f436",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "_io.TextIOWrapper"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(myFile)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "516ce7b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'test 1\\ntest 2\\ntest 3\\n'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myFile.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b4ad92ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myFile.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "22418a98",
   "metadata": {},
   "outputs": [],
   "source": [
    "myFile.seek(0) #Cursor'u en başa döndürmek için kullanılır. Manuel"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a813629c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'test 1\\ntest 2\\ntest 3\\n'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myFile.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "30105640",
   "metadata": {},
   "outputs": [],
   "source": [
    "myFile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "2213bc21",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"myfile.txt\") as myFile:\n",
    "    myContent = myFile.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "aae1b324",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'test 1\\ntest 2\\ntest 3\\n'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myContent"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ae41a16c",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"myfile.txt\", mode = \"w\") as myNewFile:\n",
    "    myNewFile.write(\"test 4\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "06b670ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"myfile.txt\", mode = \"r\") as myFile2:\n",
    "    myContent = myFile2.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c2718410",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'test 4'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myContent"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fdc911ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "#w -> write, r -> read, a -> append"
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
