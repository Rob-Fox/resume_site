
import pdfplumber, re, copy
from datetime import datetime

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
        self.sections['SKILLS & ABILITIES'] = self.clean_skills(skills)
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

        job = None

        for line in lines:
            if '|' in line:
                if job:
                    new_exp.append(copy.deepcopy(job))
                
                parts = line.split('|')
                job = {
                    'title': parts[0],
                    'company': parts[1],
                    'period': parts[2],
                    'bullets': [],
                    'start': '',
                    'end': ''
                }
            else:
                if job and line.strip():
                    stripped = line.strip()
                    if stripped.startswith('·'):
                        job['bullets'].append(line.strip())
                    elif job['bullets']:
                        job['bullets'][-1] += ' ' + stripped
        
        if job:
            new_exp.append(copy.deepcopy(job))
        for job in new_exp:
            job['start'], job['end'] = self.parse_dates(job['period'])
        return new_exp
    

    def parse_dates(self, period):
        start, end = period.split('–')
        start, end = start.strip(), end.strip()
        start = datetime.strptime(start, "%b%Y").date()
        if end != 'PRESENT':
            end = datetime.strptime(end, "%b%Y").date()
        else:
            end = None
        return start, end

    def clean_skills(self, skills):
        lines = re.sub(r'\(.*?\)', '', skills, flags=re.DOTALL)
        lines = lines.replace('\uf0b7 ', '').split('\n')
        cleaned_skills = []
        for line in lines:
            split_line = line.split(':')
            category = split_line[0]
            raw_list = re.sub(r'\/.*?\,', ',', split_line[1]).split(',')
            for item in raw_list:
                cleaned_skills.append({'category': category, 'skill': item})
        return cleaned_skills

