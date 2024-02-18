class Solution:
    def mostBooked(self, n, meetings):
        # Initialize arrays to store the count of bookings and the end times of meetings
        ans = [0] * n
        times = [0] * n

        # Sort the meetings based on their start times
        meetings.sort()

        for meeting in meetings:
            start, end = meeting
            flag = False
            minind = -1
            val = float('inf')

            # Find the earliest available slot or the meeting that ends first
            for j in range(n):
                if times[j] < val:
                    val = times[j]
                    minind = j
                if times[j] <= start:
                    flag = True
                    ans[j] += 1
                    times[j] = end
                    break
            
            # If no available slot, schedule the meeting in the earliest ending meeting's slot
            if not flag:
                ans[minind] += 1
                times[minind] += (end - start)

        # Find the index with the maximum bookings
        maxi = -1
        id = -1
        for i in range(n):
            if ans[i] > maxi:
                maxi = ans[i]
                id = i

        return id
