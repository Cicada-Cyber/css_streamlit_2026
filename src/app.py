"""
Interactive CV Portfolio - Caitlin Short
A modern, interactive CV built with Streamlit
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import pandas as pd

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Caitlin Short | Biomedical Computer Scientist",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS STYLING
# ============================================================================

def load_css():
    """Inject custom CSS for polished, modern design"""
    st.markdown("""
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
        
        /* Global Styles */
        .main {
            font-family: 'Inter', sans-serif;
        }
        
        /* Hero Section */
        .hero-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 3rem 2rem;
            border-radius: 15px;
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            line-height: 1.2;
        }
        
        .hero-subtitle {
            font-size: 1.5rem;
            font-weight: 300;
            margin-bottom: 1rem;
            opacity: 0.95;
        }
        
        .hero-location {
            font-size: 1rem;
            opacity: 0.85;
            margin-bottom: 1.5rem;
        }
        
        .hero-summary {
            font-size: 1.1rem;
            line-height: 1.6;
            max-width: 900px;
            opacity: 0.95;
        }
        
        /* Section Headers */
        .section-header {
            font-size: 2rem;
            font-weight: 600;
            color: #667eea;
            margin-top: 2rem;
            margin-bottom: 1.5rem;
            border-bottom: 3px solid #667eea;
            padding-bottom: 0.5rem;
        }
        
        /* Skill Tags */
        .skill-tag {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.4rem 1rem;
            border-radius: 20px;
            margin: 0.3rem;
            font-size: 0.9rem;
            font-weight: 500;
            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3);
        }
        
        .skill-tag-secondary {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        }
        
        .skill-tag-tertiary {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        }
        
        /* Experience Cards */
        .experience-card {
            background: white;
            border-left: 4px solid #667eea;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .experience-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 20px rgba(102, 126, 234, 0.2);
        }
        
        .job-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: #2d3748;
            margin-bottom: 0.3rem;
        }
        
        .company-name {
            font-size: 1.1rem;
            color: #667eea;
            font-weight: 500;
            margin-bottom: 0.3rem;
        }
        
        .job-duration {
            font-size: 0.9rem;
            color: #718096;
            margin-bottom: 1rem;
        }
        
        /* Stats Cards */
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 0.3rem;
        }
        
        .stat-label {
            font-size: 0.9rem;
            opacity: 0.9;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Contact Links */
        .contact-link {
            display: inline-flex;
            align-items: center;
            background: #f7fafc;
            padding: 0.8rem 1.5rem;
            border-radius: 8px;
            margin: 0.5rem;
            text-decoration: none;
            color: #2d3748;
            font-weight: 500;
            transition: all 0.2s;
            border: 2px solid #e2e8f0;
        }
        
        .contact-link:hover {
            background: #667eea;
            color: white;
            border-color: #667eea;
            transform: translateY(-2px);
        }
        
        /* Timeline */
        .timeline-item {
            position: relative;
            padding-left: 2rem;
            margin-bottom: 2rem;
        }
        
        .timeline-item::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #667eea;
            border: 3px solid white;
            box-shadow: 0 0 0 2px #667eea;
        }
        
        /* Sidebar Styling */
        .css-1d391kg {
            background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        }
        
        /* Metrics */
        [data-testid="stMetricValue"] {
            font-size: 2rem;
            color: #667eea;
        }
        
        /* Hide Streamlit Branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .animated {
            animation: fadeIn 0.6s ease-out;
        }
        </style>
    """, unsafe_allow_html=True)

# ============================================================================
# DATA CONFIGURATION
# ============================================================================

# Personal Information
PERSONAL_INFO = {
    "name": "Caitlin Short",
    "title": "Biomedical Computer Scientist",
    "location": "Stellenbosch, South Africa",
    "email": "caitlinshort4482@gmail.com",
    "linkedin": "https://www.linkedin.com/in/caitlin-short",
    "gitlab": "https://gitlab.com/caitlinshort",
    "summary": """Highly analytical Bioinformatics researcher and Data Engineer with expertise in 
    neurological data analysis and full-stack development. Combines strong technical capabilities 
    in processing large-scale biological datasets with project management experience. Currently 
    advancing research in brain aging and cognitive function while building scalable data 
    processing solutions."""
}

# Skills organized by category
SKILLS = {
    "Programming Languages": {
        "Python": 95,
        "Java": 90,
        "SQL": 90,
        "C": 75,
        "Bash": 70,
        "BigQuery": 70
    },
    "Frameworks & Tools": {
        "React": 80,
        "Svelte": 75,
        "Docker": 80,
        "Git": 90,
        "MongoDB Atlas": 85,
        "PostgreSQL": 85,
        "Terraform": 70
    },
    "Data Science": {
        "Machine Learning": 85,
        "Statistical Analysis": 90,
        "NLP": 80,
        "Data Visualization": 85,
        "GPT Integration": 75
    },
    "Bioinformatics": {
        "Protein Analysis": 90,
        "KEGG Pathway Analysis": 85,
        "MS/MS Data Processing": 90,
        "GWAS Analysis": 80
    }
}

# Work Experience
EXPERIENCE = [
    {
        "title": "MSc Neuroscience Researcher",
        "company": "BMRI, Tygerberg",
        "duration": "2025 - Current",
        "description": "Research Focus: Brain aging biomarkers, cognitive function analysis, and genetic influence studies",
        "achievements": [
            "Analysing datasets of 287+ control samples for brain age correlation studies",
            "Investigating APOE genetic variants' impact on brain aging",
            "Developing analytical pipelines for processing large-scale neurological data"
        ]
    },
    {
        "title": "Project Manager & Technical Developer",
        "company": "Glyde Payments",
        "duration": "Jun 2024 – Dec 2024",
        "description": "",
        "achievements": [
            "Led cross-functional team of 15 in implementing company-wide policies",
            "Developed RESTful APIs handling daily transactions",
            "Implemented automated SQL reporting system reducing manual reporting time by 75%",
            "Conducted security assessments identifying and resolving vulnerabilities",
            "Managed 5+ concurrent technical projects with 100% on-time delivery rate"
        ]
    },
    {
        "title": "Data Engineer / Developer",
        "company": "Intelli AI",
        "duration": "Oct 2023 - Dec 2023",
        "description": "",
        "achievements": [
            "Engineered Python-based data processing solutions for 60M+ record dataset",
            "Developed voting pattern analysis system processing data from 23,000+ voting stations",
            "Implemented NLP analysis on 25,000+ word corpus, achieving 40% reduction in redundant content",
            "Built full-stack KPI dashboard for real-time data visualization"
        ]
    },
    {
        "title": "Junior Lecturer",
        "company": "Stellenbosch University",
        "duration": "Jan 2022 - Jun 2023",
        "description": "",
        "achievements": [
            "Taught programming fundamentals to 200+ students across 3 courses",
            "Achieved 95% student satisfaction rating",
            "Evaluated 500+ programming assignments in Java, Python, C"
        ]
    },
    {
        "title": "Junior Developer",
        "company": "Stellenbosch University",
        "duration": "Jul 2022 - Dec 2022",
        "description": "",
        "achievements": [
            "Developed automated diagnostics system processing daily sensor data points",
            "Led bi-weekly project demos for team of 8 developers",
            "Achieved 98% code review approval rate"
        ]
    }
]

# Education
EDUCATION = [
    {
        "degree": "MSc Neuroscience",
        "institution": "BMRI, Tygerberg",
        "year": "2025 - Current",
        "details": "Research Focus: Brain aging biomarkers, cognitive function analysis, and genetic influence studies",
        "gpa": None
    },
    {
        "degree": "BSc Hons Bioinformatics and Computational Biology",
        "institution": "Stellenbosch University",
        "year": "2024",
        "details": "Thesis: Proteomic Analysis of Traumatic Brain Injuries",
        "gpa": 3.8,
        "highlights": [
            "Developed Python pipeline processing 1TB+ of MS/MS genetic data",
            "Implemented statistical analysis framework for protein abundance quantification",
            "Conducted KEGG pathway analysis for neurological cascade identification"
        ]
    },
    {
        "degree": "BSc Bioinformatics and Computational Biology",
        "institution": "Stellenbosch University",
        "year": "2020-2023",
        "details": "Major focus: Computational Biology, Statistics, Programming",
        "gpa": 3.2
    }
]

# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def create_skills_radar_chart(category, skills):
    """Create a radar chart for skills in a category"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=list(skills.values()),
        theta=list(skills.keys()),
        fill='toself',
        line=dict(color='#667eea', width=2),
        fillcolor='rgba(102, 126, 234, 0.3)',
        name=category
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10)
            )
        ),
        showlegend=False,
        height=400,
        margin=dict(l=80, r=80, t=40, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def create_skills_bar_chart(category, skills):
    """Create a horizontal bar chart for skills"""
    df = pd.DataFrame({
        'Skill': list(skills.keys()),
        'Proficiency': list(skills.values())
    })
    
    fig = px.bar(
        df,
        x='Proficiency',
        y='Skill',
        orientation='h',
        color='Proficiency',
        color_continuous_scale=['#764ba2', '#667eea'],
        range_color=[0, 100]
    )
    
    fig.update_layout(
        showlegend=False,
        height=max(300, len(skills) * 40),
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title="",
        yaxis_title="",
        font=dict(size=12)
    )
    
    fig.update_traces(
        marker_line_color='rgb(8,48,107)',
        marker_line_width=0,
        texttemplate='%{x}%',
        textposition='inside',
        textfont=dict(color='white', size=11, family='Inter')
    )
    
    fig.update_xaxes(range=[0, 100], showgrid=True, gridcolor='rgba(200,200,200,0.2)')
    fig.update_yaxes(showgrid=False)
    
    return fig

def create_timeline_chart():
    """Create an interactive timeline of career progression"""
    timeline_data = []
    
    for exp in EXPERIENCE:
        # Parse duration
        duration = exp['duration']
        if '–' in duration or '-' in duration:
            parts = duration.replace('–', '-').split('-')
            start = parts[0].strip()
            end = parts[1].strip() if len(parts) > 1 else "Current"
        else:
            start = duration
            end = duration
        
        timeline_data.append({
            'Position': exp['title'],
            'Company': exp['company'],
            'Start': start,
            'End': end,
            'Duration': duration
        })
    
    df = pd.DataFrame(timeline_data)
    
    # Create a simple representation
    return df

# ============================================================================
# SECTION RENDERING FUNCTIONS
# ============================================================================

def render_hero():
    """Render the hero section"""
    st.markdown(f"""
        <div class="hero-container animated">
            <div class="hero-title">{PERSONAL_INFO['name']}</div>
            <div class="hero-subtitle">{PERSONAL_INFO['title']}</div>
            <div class="hero-location">📍 {PERSONAL_INFO['location']}</div>
            <div class="hero-summary">{PERSONAL_INFO['summary']}</div>
        </div>
    """, unsafe_allow_html=True)

def render_stats():
    """Render key statistics"""
    st.markdown('<div class="section-header">📊 Career Highlights</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="stat-card animated">
                <div class="stat-number">287+</div>
                <div class="stat-label">Brain Samples Analyzed</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="stat-card animated">
                <div class="stat-number">60M+</div>
                <div class="stat-label">Records Processed</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="stat-card animated">
                <div class="stat-number">200+</div>
                <div class="stat-label">Students Taught</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class="stat-card animated">
                <div class="stat-number">1TB+</div>
                <div class="stat-label">Genetic Data Pipeline</div>
            </div>
        """, unsafe_allow_html=True)

def render_experience():
    """Render work experience section"""
    st.markdown('<div class="section-header">💼 Professional Experience</div>', unsafe_allow_html=True)
    
    for exp in EXPERIENCE:
        with st.expander(f"**{exp['title']}** at {exp['company']}", expanded=False):
            st.markdown(f"**Duration:** {exp['duration']}")
            
            if exp['description']:
                st.markdown(f"*{exp['description']}*")
            
            st.markdown("**Key Achievements:**")
            for achievement in exp['achievements']:
                st.markdown(f"• {achievement}")

def render_education():
    """Render education section"""
    st.markdown('<div class="section-header">🎓 Education</div>', unsafe_allow_html=True)
    
    for edu in EDUCATION:
        with st.expander(f"**{edu['degree']}** - {edu['institution']}", expanded=False):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**Year:** {edu['year']}")
                st.markdown(f"**Focus:** {edu['details']}")
                
                if 'highlights' in edu:
                    st.markdown("**Highlights:**")
                    for highlight in edu['highlights']:
                        st.markdown(f"• {highlight}")
            
            with col2:
                if edu['gpa']:
                    st.metric("GPA", f"{edu['gpa']}/4.0")

def render_skills():
    """Render skills section with interactive visualizations"""
    st.markdown('<div class="section-header">🛠️ Technical Skills</div>', unsafe_allow_html=True)
    
    # Category selector
    skill_categories = list(SKILLS.keys())
    
    # Create tabs for each category
    tabs = st.tabs(skill_categories)
    
    for i, category in enumerate(skill_categories):
        with tabs[i]:
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown(f"### {category}")
                fig = create_skills_bar_chart(category, SKILLS[category])
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                st.markdown("### Proficiency Overview")
                fig = create_skills_radar_chart(category, SKILLS[category])
                st.plotly_chart(fig, use_container_width=True)

def render_skills_tags():
    """Render all skills as styled tags"""
    st.markdown('<div class="section-header">💡 All Skills at a Glance</div>', unsafe_allow_html=True)
    
    colors = ['skill-tag', 'skill-tag-secondary', 'skill-tag-tertiary']
    
    for i, (category, skills) in enumerate(SKILLS.items()):
        st.markdown(f"**{category}**")
        tags_html = ""
        for skill in skills.keys():
            color_class = colors[i % len(colors)]
            tags_html += f'<span class="skill-tag {color_class}">{skill}</span>'
        st.markdown(tags_html, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

def render_contact():
    """Render contact section"""
    st.markdown('<div class="section-header">📬 Get In Touch</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <a href="mailto:{PERSONAL_INFO['email']}" class="contact-link" target="_blank">
                📧 Email
            </a>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <a href="{PERSONAL_INFO['linkedin']}" class="contact-link" target="_blank">
                💼 LinkedIn
            </a>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <a href="{PERSONAL_INFO['gitlab']}" class="contact-link" target="_blank">
                🦊 GitLab
            </a>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Contact form (demonstration - doesn't actually send)
    with st.expander("📝 Send a Message (Demo)"):
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Message", height=150)
            submit = st.form_submit_button("Send Message")
            
            if submit:
                if name and email and message:
                    st.success("✅ Message sent! (Demo mode - no actual email sent)")
                else:
                    st.error("Please fill in all fields")

def render_projects():
    """Render key projects and research"""
    st.markdown('<div class="section-header">🔬 Featured Projects & Research</div>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "Brain Aging Biomarkers Research",
            "type": "Research Project",
            "description": "Analyzing 287+ control samples to identify brain age correlation patterns and investigate APOE genetic variants' impact on brain aging.",
            "tech": ["Python", "Statistical Analysis", "GWAS", "Neuroimaging"],
            "status": "Ongoing"
        },
        {
            "title": "Proteomic Analysis Pipeline",
            "type": "MSc Thesis",
            "description": "Developed comprehensive Python pipeline for processing 1TB+ of MS/MS genetic data for traumatic brain injury research.",
            "tech": ["Python", "MS/MS", "KEGG Analysis", "Data Processing"],
            "status": "Completed"
        },
        {
            "title": "Voting Pattern Analysis System",
            "type": "Data Engineering",
            "description": "Engineered Python-based system processing 60M+ records from 23,000+ voting stations with NLP analysis reducing redundancy by 40%.",
            "tech": ["Python", "NLP", "Data Visualization", "BigQuery"],
            "status": "Completed"
        },
        {
            "title": "Automated SQL Reporting System",
            "type": "Project Management",
            "description": "Implemented automated reporting system reducing manual reporting time by 75% while managing 5+ concurrent technical projects.",
            "tech": ["SQL", "RESTful APIs", "Automation", "PostgreSQL"],
            "status": "Completed"
        }
    ]
    
    cols = st.columns(2)
    
    for i, project in enumerate(projects):
        with cols[i % 2]:
            with st.container():
                st.markdown(f"""
                    <div class="experience-card">
                        <div class="job-title">{project['title']}</div>
                        <div class="company-name">{project['type']}</div>
                        <div class="job-duration">Status: {project['status']}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown(project['description'])
                
                # Tech tags
                tech_tags = ""
                for tech in project['tech']:
                    tech_tags += f'<span class="skill-tag">{tech}</span>'
                st.markdown(tech_tags, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)

def render_achievements():
    """Render certifications and achievements"""
    st.markdown('<div class="section-header">🏆 Certifications & Achievements</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Academic & Professional**
        - 🎓 MSc Neuroscience (In Progress)
        - 🎓 BSc Hons Bioinformatics (GPA: 3.8)
        - 👨‍🏫 95% Student Satisfaction Rating
        - 📊 98% Code Review Approval Rate
        """)
    
    with col2:
        st.markdown("""
        **Certifications & Athletics**
        - 🥉 Bronze Springbok Colours in Horse Riding (National Level)
        - 🚑 Level 1 Emergency Medical Aid Certification
        - 🥏 National Level Ultimate Frisbee Player
        - 🌍 Languages: English (Native), Afrikaans (Native), French (Basic)
        """)

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

def render_sidebar():
    """Render sidebar with navigation"""
    with st.sidebar:
        st.markdown("""
            <div style='text-align: center; padding: 2rem 0;'>
                <h2 style='color: white; margin-bottom: 0.5rem;'>🧬 Navigation</h2>
                <p style='color: rgba(255,255,255,0.8); font-size: 0.9rem;'>Explore my portfolio</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation menu
        page = st.radio(
            "Go to:",
            ["🏠 Home", "💼 Experience", "🎓 Education", "🛠️ Skills", "🔬 Projects", "🏆 Achievements", "📬 Contact"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        st.markdown("""
            <div style='color: white; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 8px; margin-top: 2rem;'>
                <p style='font-size: 0.85rem; margin: 0;'>
                    <strong>💡 Tip:</strong> Click on expandable sections to see more details!
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>" * 3, unsafe_allow_html=True)
        
        st.markdown("""
            <div style='color: rgba(255,255,255,0.6); font-size: 0.75rem; text-align: center;'>
                Built with ❤️ using Streamlit<br>
                © 2025 Caitlin Short
            </div>
        """, unsafe_allow_html=True)
        
        return page

# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application function"""
    
    # Load custom CSS
    # load_css()
    
    # Render sidebar and get selected page
    selected_page = render_sidebar()
    
    # Route to appropriate page
    if selected_page == "🏠 Home":
        render_hero()
        st.markdown("<br>", unsafe_allow_html=True)
        render_stats()
        st.markdown("<br>", unsafe_allow_html=True)
        render_skills_tags()
        
    elif selected_page == "💼 Experience":
        render_hero()
        st.markdown("<br>", unsafe_allow_html=True)
        render_experience()
        
    elif selected_page == "🎓 Education":
        render_hero()
        st.markdown("<br>", unsafe_allow_html=True)
        render_education()
        
    elif selected_page == "🛠️ Skills":
        render_hero()
        st.markdown("<br>", unsafe_allow_html=True)
        render_skills()
        
    elif selected_page == "🔬 Projects":
        render_hero()
        st.markdown("<br>", unsafe_allow_html=True)
        render_projects()
        
    elif selected_page == "🏆 Achievements":
        render_hero()
        st.markdown("<br>", unsafe_allow_html=True)
        render_achievements()
        
    elif selected_page == "📬 Contact":
        render_hero()
        st.markdown("<br>", unsafe_allow_html=True)
        render_contact()
    
    # Footer
    st.markdown("<br>" * 2, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #718096; font-size: 0.85rem;'>
            <p>Thank you for viewing my portfolio! Feel free to reach out for collaborations or opportunities.</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()