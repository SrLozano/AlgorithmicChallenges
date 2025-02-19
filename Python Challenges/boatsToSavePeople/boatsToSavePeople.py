class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        needed_boats = 0
        l, r = 0, len(people) - 1

        while l <= r:
            remaining = limit  - people[r]
            r -= 1
            needed_boats += 1

            if people[l] <= remaining:
                l += 1

        return needed_boats
