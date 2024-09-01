import art
from candidate import Candidate
from batch import BatchAllocator
from Gen_AI import GenAIIntegration


def main():
    batch_allocator = BatchAllocator()
    ai_integration = GenAIIntegration("https://console.groq.com/keys")
    candidates = []

    while True:
        print("Register a new candidate")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        degree = input("Enter Degree: ")
        specialization = input("Enter Specialization: ")
        phone = input("Enter Phone Number: ")
        certifications = input("Enter Certifications (comma separated): ").lower().split(", ")
        internship_details = input("Enter Internship Details: ")
        courses = input("Enter Courses (comma separated): ").lower().split(", ")
        linkedin = input("Enter LinkedIn: ")
        github = input("Enter GitHub: ")
        languages = input("Enter Languages (comma separated): ").split(", ")

        candidate = Candidate(name, email, degree, specialization, phone, certifications, internship_details, courses, linkedin, github, languages)

        if candidate.is_valid():
            ai_integration.determine_batch(candidate)
            batch_allocator.allocate_to_batch(candidate)
            candidates.append(candidate)
        else:
            print("Candidate data is incomplete or invalid. Please try again.")

        another = input("Register another candidate? (y/n): ").lower()
        if another != 'y':
            break

    batches = batch_allocator.finalize_batches()
    print("\nBatch Allocation Completed!")
    for batch_name, batch_list in batches.items():
        for batch in batch_list:
            print(f"{batch['id']} - Members: {len(batch['members'])}")

    print("\nRegistered Candidates Details:")
    for candidate in candidates:
        details = candidate.get_details()
        print(f"Name: {details['name']}, Batch: {details['batch']}")

if __name__ == "__main__":
    main()