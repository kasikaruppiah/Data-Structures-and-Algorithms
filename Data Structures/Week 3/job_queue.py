# python3

class JobQueue:
    def read_data(self):
        self.num_workers, self.num_jobs = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert self.num_jobs == len(self.jobs)

    def write_response(self):
        for i in range(self.num_jobs):
          print(self.assigned_workers[i], self.start_times[i]) 

    def sift_down(self, i):
        minIndex = i
        l = 2 * i + 1
        if l < self.num_workers and (self.next_free_time[l][0] < self.next_free_time[minIndex][0] or (self.next_free_time[l][0] == self.next_free_time[minIndex][0] and self.next_free_time[l][1] < self.next_free_time[minIndex][1])):
          minIndex = l
        r = 2 * i + 2
        if r < self.num_workers and (self.next_free_time[r][0] < self.next_free_time[minIndex][0] or (self.next_free_time[r][0] == self.next_free_time[minIndex][0] and self.next_free_time[r][1] < self.next_free_time[minIndex][1])):
          minIndex = r
        if i != minIndex:
          self.next_free_time[i], self.next_free_time[minIndex] = self.next_free_time[minIndex], self.next_free_time[i]
          self.sift_down(minIndex)

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * self.num_jobs
        self.start_times = [None] * self.num_jobs
        self.next_free_time = [(0, i) for i in range(self.num_workers)]
        for i in range(self.num_jobs):
          self.assigned_workers[i] = self.next_free_time[0][1]
          self.start_times[i] = self.next_free_time[0][0]
          self.next_free_time[0] = (self.next_free_time[0][0] + self.jobs[i], self.next_free_time[0][1])
          self.sift_down(0)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
