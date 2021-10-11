# Hashmap

## **note: language of choice is python**

### https://developers.google.com/edu/python/dict-files

- "key/value hash table" -> dict
- dict = { key1 : value1, key2 : value2, ...}
- dict[key1] gives value1; throws KeyError if not in dict
- use dict.get(key), returns None is key is not found
- or dict.get(key, not-found) to specify what value to return if key is not found
- or val = dict[key1] if key1 in dict else -1



- 1). hash function design: the purpose of hash function is to map a key value to an address in the storage space, similarly to the system that we assign a postcode to each mail address. As one can image, for a good hash function, it should map different keys evenly across the storage space, so that we don't end up with the case that the majority of the keys are concentrated in a few spaces.
- 2). collision handling: essentially the hash function reduces the vast key space into a limited address space. As a result, there could be the case where two different keys are mapped to the same address, which is what we call 'collision'. Since the collision is inevitable, it is important that we have a strategy to handle the collision.
