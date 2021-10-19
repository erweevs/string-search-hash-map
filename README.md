# String Search Hash Map
The objective is to relevant strings, that are not hindered by typos.

### How to implement this functionality
1. For each string, construct a 26 element vector, where each vector element represents tehe frequency the given letter occurs.
2. Use this vector as a key for inserting strings into the Hash Map.
3. Store the list of the calculated character counts as the key, and the string as the value.
4. Retrun the values of each Hash Map.