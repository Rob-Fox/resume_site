
import pdfplumber, re

class ResumeParser:
    def __init__(self, pdf):
        self.pdf = pdf
        self.headers = [
            'HEADER',
            'EXPERIENCE',
            'SKILLS & ABILITIES'
        ]


    def extract_text(self):
        self.text = ''
        with pdfplumber.open(self.pdf) as pdf:
            for page in pdf.pages:
                self.text += page.extract_text() + '\n'
        return self


    def normalize(self):
        self.text = self.text.replace('\r', '\n')
        self.text = re.sub(r'\n{2,}', '\n', self.text)
        self.text = re.sub(r'[ \t]+', ' ', self.text)
        self.text = self.text.strip()
        return self


    def split_sections(self):
        lines = self.text.split('\n')
        sections = {}
        current_section = 'HEADER'
        sections[current_section] = []

        for line in lines:
            cleaned = line.strip().lower()

            if cleaned.upper() in self.headers:
                current_section = cleaned.upper()
                sections[current_section] = []
            else:
                sections[current_section].append(line)
        for key in sections:
            sections[key] = '\n'.join(sections[key]).strip()
        
        self.sections = sections
        return self


    def clean_sections(self):
        header = self.sections['HEADER']
        experience = self.sections['EXPERIENCE']
        skills = self.sections['SKILLS & ABILITIES']
        self.sections['HEADER'] = self.clean_header(header)
        self.sections['EXPERIENCE'] = self.clean_experience(experience)
        return self


    def clean_header(self, header):
        lines = header.split('\n')
        new_header = {
            'name': '',
            'title': '',
            'email': '',
            'phone': '',
            'location': '',
            'socials': '',
            'blurb': ''
        }
        new_header['name'] = lines[0]
        new_header['title'] = lines[1]
        new_header['location'] = lines[2]
        new_header['phone'] = lines[3]
        new_header['blurb'] = lines[5] + ' '+ lines[6]
        socials = lines[4].split('|')
        new_header['email'] = socials[0]
        new_header['socials'] = socials[1:]
        return new_header

    
    def clean_experience(self, experience):
        new_exp = []
        lines = experience.split('\n')
        print(f'### UNSPLIT: {repr(experience)}')
        for line in lines:
            job = {
                'title': '',
                'company': '',
                'period': '',
                'bullets': []
            }
            if '|' in line:
                line = line.split('|')
                job['title'] = line[0]
                job['company'] = line[1]
                job['period'] = line[2]
                # lines = lines.join()
            
            print(f'### {line}')