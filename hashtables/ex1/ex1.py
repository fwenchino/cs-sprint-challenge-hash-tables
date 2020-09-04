def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    # check if value in caché
    if limit in cache:
        return cache[limit]

    else:
        # Calculate the entry to the caché
        entry = None

        for i1, w1 in enumerate(weights):
            w2 = limit - w1

            if w2 in weights:
                if w2 != w1:
                    i2 = weights.index(w2)
                else:
                    weights[i1] = w1 + 1
                    i2 = weights.index(w2)

                if i1 > i2:
                    entry = (i1, i2)
                    break
                else:
                    entry = (i2, i1)
                    break

        cache[limit] = entry

    return entry

print(get_indices_of_item_weights([4, 4], 2, 8))