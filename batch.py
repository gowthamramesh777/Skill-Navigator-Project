class BatchAllocator:
    def __init__(self, min_batch_size=25, max_batch_size=30):
        self.batches = {
            'Data Engineering': [],
            'Java': [],
            '.NET': []
        }
        self.current_batch = {
            'Data Engineering': [],
            'Java': [],
            '.NET': []
        }
        self.batch_id_counter = {
            'Data Engineering': 1,
            'Java': 1,
            '.NET': 1
        }
        self.min_batch_size = min_batch_size
        self.max_batch_size = max_batch_size

    def create_new_batch(self, batch_name):
        batch_id = f"{batch_name}-Batch-{self.batch_id_counter[batch_name]}"
        self.batches[batch_name].append({
            'id': batch_id,
            'members': self.current_batch[batch_name]
        })
        self.batch_id_counter[batch_name] += 1
        self.current_batch[batch_name] = []

    def allocate_to_batch(self, candidate):
        batch_name = candidate.batch_name
        if batch_name not in self.batches:
            print(f"Invalid batch type: {batch_name}")
            return

        current_batch = self.current_batch[batch_name]

        if len(current_batch) >= self.max_batch_size:
            self.create_new_batch(batch_name)

        self.current_batch[batch_name].append(candidate)

        if len(self.current_batch[batch_name]) >= self.max_batch_size:
            self.create_new_batch(batch_name)

        print(f"Candidate {candidate.name} allocated to {batch_name} batch.")

    def finalize_batches(self):
        for batch_name, batch_list in self.batches.items():
            if self.current_batch[batch_name] and len(self.current_batch[batch_name]) >= self.min_batch_size:
                self.create_new_batch(batch_name)

        return {
            batch_name: batch_list
            for batch_name, batch_list in self.batches.items()
            if batch_list
        }
