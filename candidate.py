
class Candidate:
    def __init__(self, name, email, degree, specialization, phone, certifications, internship_details, courses, linkedin, github, languages):
        self.name = name
        self.email = email
        self.degree = degree
        self.specialization = specialization
        self.phone = phone
        self.certifications = certifications
        self.internship_details = internship_details
        self.courses = courses
        self.linkedin = linkedin
        self.github = github
        self.languages = languages
        self.batch_name = self.determine_batch()

    def is_valid(self):
        return all([self.name, self.email, self.degree, self.specialization, self.phone])

    def determine_batch(self):
        if 'python' in self.certifications:
            return 'Data Engineering'
        elif 'java' in self.certifications or 'aws' in self.certifications:
            return 'Java'
        elif 'azure' in self.certifications or '.net' in self.certifications:
            return '.net'
        else:
            return None

    def get_details(self):
        return {
            'name': self.name,
            'email': self.email,
            'degree': self.degree,
            'specialization': self.specialization,
            'phone': self.phone,
            'certifications': self.certifications,
            'internship_details': self.internship_details,
            'courses': self.courses,
            'linkedin': self.linkedin,
            'github': self.github,
            'languages': self.languages,
            'batch': self.batch_name
        }
