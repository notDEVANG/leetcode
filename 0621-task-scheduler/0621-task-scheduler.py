class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)

        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        queue = deque()
        time = 0
        
        while heap or queue:
            time += 1

            if queue and queue[0][1] <= time:
                freq, available_time = queue.popleft()
                heapq.heappush(heap, freq)

            if heap:
                freq = heapq.heappop(heap)
                freq += 1

                if freq < 0:
                    queue.append((freq, time + n + 1))

        return time