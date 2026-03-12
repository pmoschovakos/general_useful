def find_subsets(numbers, target):
    # 1. ΤΑΞΙΝΟΜΗΣΗ 
    numbers.sort(reverse=True)
    
    # 2 Look-ahead / Suffix Sums,  done once
    suffix_sums = [0] * len(numbers)
    current_total = 0
    #suffix_sums sums the list in reverse
    for i in range(len(numbers) - 1, -1, -1):
        current_total += numbers[i]
        suffix_sums[i] = current_total

    valid_subsets = [] #array for storage of results 

    # 3. core
    # start_index: list's starting position
    # current_subset: numbers already used
    # current_sum: sum of current subset
    def backtrack(start_index, current_subset, current_sum):
        
        # stoping sequence
        if current_sum == target:
            # we use a copy of the list in order to be able to use it simultanusly on another branch
            # when we get target sum process is terminated
            valid_subsets.append(list(current_subset))
            return #returning to search anew
        
        # Branch and Bound
        # trying all numbers starting from: start_index.
        for i in range(start_index, len(numbers)):
            
            # Upper Bound (cut 1)
            # Basically if next number excedes the sum target immediately look for a smaller one  
            if current_sum + numbers[i] > target:
                continue 
                
            # Lower Bound (cut 2)
            # checks if we can even reach the target if all the following nubers are summed, if not, branch elliminated (break)
            if current_sum + suffix_sums[i] < target:
                break 
            
            # step 1, starting number.
            current_subset.append(numbers[i])
                
            # step 2 backtracking: calling myself to find the next number to sum
            backtrack(i + 1, current_subset, current_sum + numbers[i])
            # step 3 emptying to continue for function 
            current_subset.pop()

    # zeroing the indexes to begin
    backtrack(0, [], 0)
    
    return valid_subsets

# -- execution --
dataset = [18897109, 12828837, 9461105, 6371773, 5965343, 5946800, 5582170, 5564635,
5268860, 4552402, 4335391, 4296250, 4224851, 4192887, 3439809, 3279833,
3095313, 2812896, 2783243, 2710489, 2543482, 2356285, 2226009, 2149127,
2142508, 2134411]

target_value = 100000000 #setting the target value to 100million as asked

print("Ψάχνω για συνδυασμούς...\n")
results = find_subsets(dataset, target_value)

print(f"Βρέθηκαν συνολικά: {len(results)} λύσεις.\n")
for index, subset in enumerate(results, 1):
    print(f"Λύση {index}: {subset}")