"""Initial records copied from the public HTML pages.

These are only inserted when a table is empty, so changes made in Flask-Admin
are never overwritten on later application starts.
"""
from datetime import date

from app import db
from app.models.investment import Investment
from app.models.news import News
from app.models.project import Project
from app.models.publication import Publication
from app.models.service import Service
from app.models.stand import Stand
from app.models.vacancy import Vacancy
from app.models.page_section import PageSection
from app.models.council_member import CouncilMember
from app.models.award import Award


def _add_when_empty(model, records):
    if model.query.count() == 0:
        db.session.add_all(model(**record) for record in records)


def seed_initial_content():
    _add_when_empty(CouncilMember, [
        {"name": "Cllr. Chikwanda", "position": "Council Chairperson", "group": "Council", "ward_or_role": "Ward 1", "image_url": "https://mudzirdc.org.zw/images/chairman.jpg", "display_order": 1},
        {"name": "Cllr. Vice Chairperson", "position": "Vice Council Chairperson", "group": "Council", "ward_or_role": "Ward 2", "image_url": "https://hwedzardc.org/images/vicechairman.jpg", "display_order": 2},
        {"name": "Cllr. Ward 3", "position": "Councillor", "group": "Council", "ward_or_role": "Ward 3", "image_url": "https://mudzirdc.org.zw/images/councillor.jpg", "display_order": 3},
        {"name": "Cllr. Ward 4", "position": "Councillor", "group": "Council", "ward_or_role": "Ward 4", "image_url": "https://mudzirdc.org.zw/images/councillor.jpg", "display_order": 4},
        {"name": "Mr. T. Chinyoka", "position": "Chief Executive Officer", "group": "Management", "ward_or_role": "Overall council administration", "image_url": "https://hwedzardc.org/images/CEO.jpg", "display_order": 1},
        {"name": "Finance Director", "position": "Director of Finance", "group": "Management", "ward_or_role": "Financial management & planning", "image_url": "https://hwedzardc.org/images/finance.jpg", "display_order": 2},
        {"name": "Engineering Director", "position": "Director of Engineering", "group": "Management", "ward_or_role": "Infrastructure & roads", "image_url": "https://hwedzardc.org/images/engineering.jpg", "display_order": 3},
    ])
    _add_when_empty(Award, [
        {"title": "Best Performing Rural District Council", "description": "Awarded for outstanding service delivery and revenue collection performance among rural district councils in Mashonaland East Province.", "icon": "fa-trophy", "display_order": 1},
        {"title": "Clean Audit Award", "description": "Recognized for maintaining clean audit records and transparent financial management in local government operations.", "icon": "fa-award", "display_order": 2},
        {"title": "Community Development Excellence", "description": "Acknowledged for innovative community development programs that have improved livelihoods across the district.", "icon": "fa-medal", "display_order": 3},
        {"title": "Environmental Stewardship Award", "description": "Recognized for outstanding efforts in environmental conservation, tree planting programs and sustainable land management.", "icon": "fa-star", "display_order": 4},
        {"title": "Infrastructure Development", "description": "Commended for significant progress in roads rehabilitation, water supply systems and construction of public facilities.", "icon": "fa-certificate", "display_order": 5},
        {"title": "Stakeholder Engagement", "description": "Praised for exemplary stakeholder engagement and participatory governance practices in the district.", "icon": "fa-handshake", "display_order": 6},
    ])
    _add_when_empty(PageSection, [
        {"page": "home", "section_key": "hero", "title": "A district with an upper-middle income community by 2030.", "subtitle": "Welcome to MUDZI RDC", "content": "We deliver inclusive, responsive and transparent local government services that help residents thrive."},
        {"page": "home", "section_key": "vision", "title": "Vision", "content": "A district with an upper-middle income community by 2030.", "display_order": 1},
        {"page": "home", "section_key": "mission", "title": "Mission", "content": "To provide sustainable and quality services to the community.", "display_order": 2},
        {"page": "home", "section_key": "core-values", "title": "Core Values", "content": "Team work, responsiveness, Hunhu/Ubuntu, commitment and transparency.", "display_order": 3},
        {"page": "governance", "section_key": "introduction", "title": "Governance", "subtitle": "Transparent leadership and accountable administration for the people of Mudzi District.", "content": "The Council is composed of elected councillors who work with the management team to deliver quality services and sustainable development."},
        {"page": "contact", "section_key": "contact-details", "title": "Our Contact Information", "content": "Stand Number 1, Kotwa Growth Point\nMudzi, Mashonaland East Province\nZimbabwe\n\n+263 71 382 5999\n\nmudzirdc2015@gmail.com\n\nMonday - Friday: 07:30 - 16:30"},
    ])
    for section in [
        {"page": "payment", "section_key": "bank-transfer", "title": "Bank Transfer", "content": "Bank: CBZ Bank\nAccount Name: Mudzi Rural District Council\nAccount Number: 01520078540030\nBranch: Marondera", "display_order": 1},
        {"page": "payment", "section_key": "zimswitch-zipit", "title": "ZimSwitch / ZIPIT", "content": "Use your bank card or ZIPIT transfer. Visit any bank branch or use internet banking to transfer funds to the Mudzi RDC account.", "display_order": 2},
        {"page": "payment", "section_key": "cash-office", "title": "Cash at Our Offices", "content": "Location: Stand Number 1, Kotwa Growth Point\nHours: Mon-Fri, 07:45 - 16:45\nReceipts are issued immediately for all payments.", "display_order": 3},
    ]:
        if not PageSection.query.filter_by(page=section["page"], section_key=section["section_key"]).first():
            db.session.add(PageSection(**section))
    _add_when_empty(Service, [
        {"name": "Education", "description": "Improving access to quality education through infrastructure, resources, and teacher support.", "icon": "https://hwedzardc.org/images/Tongogara%20ICT%20bLOCK.jpeg"},
        {"name": "Health Services", "description": "Expanding healthcare access through new facilities, equipment, and community outreach.", "icon": "https://hwedzardc.org/images/Madzimbahwe.jpeg"},
        {"name": "Roads Infrastructure", "description": "Upgrading roads and bridges to improve connectivity and access to services.", "icon": "https://hwedzardc.org/images/road2.jpeg"},
        {"name": "Water & Sanitation", "description": "Providing clean water, sanitation, and hygiene facilities to improve public health.", "icon": "https://hwedzardc.org/images/rig.jpg"},
        {"name": "Public Safety", "description": "Strengthening disaster preparedness and community protection across all wards.", "icon": "https://hwedzardc.org/images/firetender.jpg"},
        {"name": "Environment Protection", "description": "Protecting forests, biodiversity, and ecosystems while promoting green energy and tourism.", "icon": "https://hwedzardc.org/images/TREE%20P%20CEO.jpeg"},
    ])
    _add_when_empty(News, [
        {"title": "Refuse Collection Services Enhanced", "category": "Waste Management", "summary": "Mudzi Rural District Council has enhanced its refuse collection services with new equipment.", "content": "Residents are encouraged to use designated refuse collection points and separate waste for recycling where possible.", "image_url": "https://hwedzardc.org/images/busss.jpeg"},
        {"title": "Mudzi RDC Selects New Junior Council", "category": "Council Leadership", "summary": "The 2026 Junior Council induction was held at Mudzi Lodge and Conference Centre.", "content": "The Junior Council platform promotes participatory democracy, youth representation and child rights.", "image_url": "https://hwedzardc.org/images/juniorcouncillors.jpg"},
        {"title": "Launch of 30 Million Tree National Planting Programme", "category": "Environment", "summary": "Over 2,000 trees were planted during the district launch campaign.", "content": "The programme supports environmental sustainability and combats deforestation.", "image_url": "https://hwedzardc.org/images/TREE%20P%20CEO.jpeg"},
        {"title": "New Traffic Innovation at Marondera-Wedza-Sadza Intersection", "category": "Road Safety", "summary": "The first overhead traffic light in the district improves safety for motorists and pedestrians.", "content": "The installation is a step towards modern road safety and traffic management.", "image_url": "https://hwedzardc.org/images/trafficlight.jpg"},
        {"title": "Community Alert - Do Not Cross Flooded Rivers", "category": "Community Alert", "summary": "Crossing flooded rivers is dangerous and can lead to loss of life and property.", "content": "Wait for water levels to subside and report emergencies to the nearest police station or council office.", "image_url": "https://hwedzardc.org/images/flood.jpeg"},
    ])
    _add_when_empty(Project, [
        {"name": "Road Rehabilitation Programme", "category": "Infrastructure", "description": "Comprehensive road rehabilitation, grading, gravelling and culvert installation on major feeder roads.", "status": "Ongoing", "image_url": "https://hwedzardc.org/images/road2.jpeg"},
        {"name": "Borehole Drilling & Water Supply", "category": "Water", "description": "New boreholes and rehabilitation of water points for underserved communities and schools.", "status": "Ongoing", "image_url": "https://hwedzardc.org/images/rig.jpg"},
        {"name": "School Infrastructure Development", "category": "Education", "description": "New classroom blocks, ICT centres and ablution facilities at schools across the district.", "status": "Ongoing", "image_url": "https://hwedzardc.org/images/Tongogara%20ICT%20bLOCK.jpeg"},
        {"name": "Madzimbahwe Health Centre", "category": "Health", "description": "Modern health centre serving over 5,000 community members with primary healthcare services.", "status": "Completed", "image_url": "https://hwedzardc.org/images/Madzimbahwe.jpeg"},
        {"name": "Solar Street Lighting", "category": "Energy", "description": "Solar-powered street lights in Kotwa Growth Point and surrounding business centres.", "status": "Upcoming", "image_url": "https://hwedzardc.org/images/solarproject.jpg"},
    ])
    _add_when_empty(Publication, [
        {"title": "Client Charter", "description": "MRDC service standards and commitments", "document_url": "#"},
        {"title": "Master Plan", "description": "MRDC district development master plan", "document_url": "#"},
        {"title": "Strategic Plan 2025", "description": "Strategic management plan reviewed 2025", "document_url": "#"},
        {"title": "Annual Plan", "description": "Current year annual development plan", "document_url": "#"},
        {"title": "Budget Report", "description": "Annual budget allocation and expenditure", "document_url": "#"},
    ])
    _add_when_empty(Investment, [
        {"title": "Agriculture", "sector": "Agriculture", "description": "Commercial farming, irrigation, agro-processing, livestock and horticulture opportunities.", "image_url": "https://hwedzardc.org/images/agriculture.jpg"},
        {"title": "Mining", "sector": "Mining", "description": "Gold, chrome, stone quarrying and mineral exploration opportunities.", "image_url": "https://hwedzardc.org/images/mining.jpg"},
        {"title": "Tourism", "sector": "Tourism", "description": "Eco-tourism, adventure, cultural tourism and conference facilities.", "image_url": "https://hwedzardc.org/images/tourism.jpg"},
    ])
    _add_when_empty(Stand, [
        {"name": "Kotwa Growth Point - Phase 1", "stand_type": "Residential", "location": "Kotwa Growth Point", "description": "Serviced residential stands with water and road access.", "size": "300m² to 500m²", "price": 500, "status": "Available"},
        {"name": "Kotwa Growth Point - Phase 2", "stand_type": "Residential", "location": "Kotwa Growth Point", "description": "New development with modern infrastructure planning.", "size": "400m² to 600m²", "price": 650, "status": "Available"},
        {"name": "Kotwa CBD - Commercial", "stand_type": "Commercial", "location": "Kotwa CBD", "description": "Prime commercial stands for retail, offices and service businesses.", "price": 1200, "status": "Available"},
    ])
    _add_when_empty(Vacancy, [
        {"title": "District Administrator", "department": "Administration", "location": "Kotwa Growth Point", "closing_date": date(2026, 4, 30), "overview": "Lead the administrative functions of the council secretariat and coordinate departmental activities.", "duties": "Coordinate council departments\nPrepare reports to Full Council\nImplement council resolutions", "qualifications": "Degree in Public Administration or related field\nAt least 5 years' experience", "application_instructions": "Submit an application letter, CV and certified copies to the Human Resources Officer or careers@mudzirdc.org.zw."},
        {"title": "Environmental Health Officer", "department": "Health", "location": "Mudzi District", "closing_date": date(2026, 5, 15), "overview": "Promote public health and environmental safety across Mudzi District.", "duties": "Conduct premises inspections\nEnforce health by-laws\nSupport health promotion programmes", "qualifications": "Degree or HND in Environmental Health\nAt least 3 years' experience", "application_instructions": "Submit an application letter, CV and certified copies to the Human Resources Officer."},
        {"title": "Accountant", "department": "Finance", "location": "Kotwa Growth Point", "closing_date": date(2026, 4, 30), "overview": "Manage council financial records, controls, budgets and reports.", "duties": "Maintain financial records\nPrepare budgets and reports", "qualifications": "Accounting qualification\nRelevant public finance experience", "application_instructions": "Submit an application letter, CV and certified copies to the Human Resources Officer."},
        {"title": "Roads & Works Engineer", "department": "Engineering", "location": "Mudzi District", "closing_date": date(2026, 5, 22), "overview": "Plan, construct and maintain district roads, bridges and council infrastructure.", "duties": "Supervise road works\nPrepare tender documents", "qualifications": "Civil engineering qualification\nAt least 4 years' experience", "application_instructions": "Submit an application letter, CV and certified copies to the Human Resources Officer."},
        {"title": "Agritex Officer", "department": "Agriculture", "location": "Mudzi District", "closing_date": date(2026, 4, 30), "overview": "Provide agricultural extension support to communities across the district.", "duties": "Advise on crop and livestock production\nSupport farmer training", "qualifications": "Agricultural qualification\nAt least 3 years' extension experience", "application_instructions": "Submit an application letter, CV and certified copies to the Human Resources Officer."},
    ])
    db.session.commit()
