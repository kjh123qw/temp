from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'skillData': {
            '언어': {
                'id': 'Languages',
                'skills':
                [
                    ['Java', 'Java'],
                    ['Python', 'Python'],
                    ['C', 'Clang'],
                    ['C#', 'CS'],
                    ['C++', 'Cpp'],
                    ['Go', 'Go'],
                    ['Kotlin', 'Kotlin'],
                    ['JavaScript', 'JavaScript'],
                    ['HTML', 'HTML'],
                    ['CSS', 'CSS'],
                    ['PHP', 'PHP'],
                    ['JSP', 'JSP'],
                    ['TypeScript', 'TypeScript'],
                    ['Rupy', 'Rupy'],
                    ['Scala', 'Scala'],
                ]
            },
            '웹 개발': {
                'id': 'WEB',
                'skills':
                [
                    ['Spring', 'Spring'],
                    ['Django', 'Django'],
                    ['Vue.js', 'Vue'],
                    ['Angular.js', 'Angular'],
                    ['.NET', 'DotNet'],
                    ['ASP.NET', 'ASPDot'],
                    ['Rails', 'Rails'],
                    ['jQuery', 'JQuery'],
                    ['React.js', 'React'],
                    ['Redux', 'Redux'],
                    ['Node.js', 'Node'],
                    ['ASP', 'ASP'],
                    ['Webpack', 'Webpack'],
                    ['Ajax', 'Ajax'],
                ]
            },
            '앱 개발': {
                'id': 'APPS',
                'skills': [
                    ['IOS', 'IOS'],
                    ['Android', 'Android'],
                    ['Swift', 'Swift'],
                    ['React Native', 'React Native'],
                ]
            },
            'DB': {
                'id': 'DB',
                'skills': [
                    ['Oracle', 'Oracle'],
                    ['MySQL', 'MySQL'],
                    ['MsSQL', 'MsSQL'],
                    ['NoSQL', 'NoSQL'],
                    ['MariaDB', 'MariaDB'],
                    ['PostgreSQL', 'PostgreSQL'],
                    ['MongoDB', 'MongoDB'],
                    ['Redis', 'Redis'],
                    ['GraphQL', 'GraphQL'],
                ]
            },
            'AI': {
                'id': 'AI',
                'skills': [
                    ['Machine Learning', 'ML'],
                    ['Deep Learning', 'DL'],
                    ['CV', 'CV'],
                    ['PyTorch', 'Pytorch'],
                    ['TensorFlow', 'Tensor'],
                ]
            },
            '빅데이터, 서버': {
                'id': 'BigSer',
                'skills': [
                    ['Linux', 'Linux'],
                    ['Docker', 'Docker'],
                    ['Kubernetes', 'Kubernetes'],
                    ['Hadoop', 'Hadoop'],
                    ['Spark', 'Spark'],
                    ['Zeplin', 'Zeplin'],
                    ['Kafka', 'Kafka'],
                    ['WAS', 'WAS'],
                    ['AWS', 'AWS'],
                    ['GCP', 'GCP'],
                    ['Azure', 'Azure'],
                ]
            },
            '협업 툴': {
                'id': 'Coll',
                'skills': [
                    ['Git', 'Git'],
                    ['JIRA', 'JIRA'],
                    ['Jenkins', 'Jenkins'],
                    ['Slack', 'Slack'],
                ]
            },
            '기타': {
                'id': 'ETC',
                'skills': [
                    ['Photoshop', 'Photoshop'],
                    ['Sketch', 'Sketch'],
                    ['Illustrator', 'Illustrator'],
                    ['Unity3D', 'Unity3D'],
                    ['Maya', 'Maya'],
                ]
            }
        },
        'jobData': [
            ['CRM', 'CRM'],
            ['DBA', 'DBA'],
            ['ERP', 'ERP'],
            ['UI/UX/GUI', 'UIUX'],
            ['게임개발', 'Game'],
            ['광고/시각디자인', 'Adver'],
            ['그래픽', 'Graphic'],
            ['네트워크/보안/운영', 'Network'],
            ['데이터분석', 'Data'],
            ['모바일앱개발', 'Mobile'],
            ['반도체/디스플레이', 'Semicon'],
            ['소프트웨어아키텍트', 'Archi'],
            ['소프트웨어엔지니어', 'Engineer'],
            ['시스템엔지니어', 'System'],
            ['시장조사/분석', 'Market'],
            ['애니메이션디자인', 'Anim'],
            ['영상/모션디자인', 'Video'],
            ['온라인마케팅', 'OnMarket'],
            ['웹개발', 'WEB'],
            ['웹디자인', 'WebDe'],
            ['웹퍼블리셔', 'WebPu'],
            ['유지/수리/정비', 'Mainte'],
            ['일러스트레이터', 'Illust'],
            ['컨설팅', 'Consult'],
            ['프로젝트매니저', 'ProMana'],
            ['하드웨어엔지니어', 'Hardw'],
        ]
    }
    return render(request, 'recommend/index.html', context)


testJobData1 = [
    ['(주)아이패밀리에스씨', '서울', '기술연구소 NodeJS 개발자', '웹개발', 'MYSQL, nodejs, 백엔드 개발'],
    ['(주)아이패밀리에스씨', '서울', '기술연구소 NodeJS 개발자', '웹개발', 'MYSQL, nodejs, 백엔드 개발'],
    ['(주)아이패밀리에스씨', '서울', '기술연구소 NodeJS 개발자', '웹개발', 'MYSQL, nodejs, 백엔드 개발'],
    ['(주)아이패밀리에스씨', '서울', '기술연구소 NodeJS 개발자', '웹개발', 'MYSQL, nodejs, 백엔드 개발'],
    ['(주)아이패밀리에스씨', '서울', '기술연구소 NodeJS 개발자', '웹개발', 'MYSQL, nodejs, 백엔드 개발'],
]
testJobData2 = [
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
]
testJobData3 = [
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
    ['에이알텍(주)', '서울', 'Windows 기반 어플리케이션 연구개발 분야 채용',
     '모바일앱개발, 소프트웨어엔지니어, 하드웨어엔지니어', 'C#, c, C++, TCP, IP, Visual studio'],
]


def resultJob(request, kind):
    skills = request.GET.getlist('skills', None)
    first = request.GET.get('first', None)
    second = request.GET.get('second', None)
    third = request.GET.get('third', None)
    job1 = request.GET.get('job1', None)
    job2 = request.GET.get('job2', None)
    job3 = request.GET.get('job3', None)
    cotext = {
        'context': {
            'kind': kind,
            'skills': skills,
            'first': first,
            'second': second,
            'third': third,
            'jobData1': testJobData1,
            'jobData2': testJobData2,
            'jobData3': testJobData3,
            'job1': job1,
            'job2': job2,
            'job3': job3,
        }
    }
    return render(request, 'recommend/result_job.html', cotext)
