from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = Dash(__name__)

# Expanded data with all subjects and faculty members under each coordinator
data = {
    'Coordinator': [
        'Dr. Amrit Kumar Agrawal', 'Dr. Amrit Kumar Agrawal', 'Dr. Amrit Kumar Agrawal', 'Dr. Amrit Kumar Agrawal',
        'Dr. Amrit Kumar Agrawal', 'Dr. Amrit Kumar Agrawal',
        'Dr. Rajendra Kumar', 'Dr. Rajendra Kumar', 'Dr. Rajendra Kumar', 'Dr. Rajendra Kumar',
        'Dr. Rajendra Kumar', 'Dr. Rajendra Kumar',
        'Dr. Kusum Lata', 'Dr. Kusum Lata', 'Dr. Kusum Lata', 'Dr. Kusum Lata',
        'Dr. Kusum Lata', 'Dr. Kusum Lata'
    ],
    'Subject': [
        'BTY223 Introduction to Biology for Engineers', 'CSE245 Discrete Structures', 
        'CSE247 Computer Organization and Architecture', 'CSE252 Computer Networks', 
        'CSE253 Object Oriented Programming Using Java', 'CSE254 Principles of Operating System',
        'CSE356 Design and Analysis of Algorithm', 'CSE357 Software Engineering and Testing Methodologies', 
        'CSE021 Introduction to Cloud Computing', 'CSE023 Android Application Development', 
        'CSE354 Web Technologies', 'BRM003 Research Methodology',
        'CSE062 Mobile Computing', 'CSE472 Artificial Intelligence', 
        'CSE063 Quantum Computing', 'CSE073 3D Printing and Software Tools',
        'CSE071 Introduction to Internet of Things', 'CSC401 Introduction to IoT & its Security'
    ],
    'Faculty': [
        'Dr. Prachi Yadav, Ms. Mohini Vats, Mr. Praveen Yadav, Dr. Azizur Rahman, Dr. Prasun Kumar, Prof. Rajesh Kannan',
        'Dr. Manmohan Singh Yadav, Dr. Anjali, Dr. Saurabh Kumar, Dr. Ashish Chakraverti, Dr. Vasudha Arora, Mr. Ajai Verma, Mr. Amit Kumar Rai, Mr. Arunkant Dwivedi, Mr. Ashish Jain, Mr. Durgesh Kumar, Mr. Pankaj Sharma, Mr. Rajiv Nath, Ms. Deepti Sahu, Ms. Ekta Singh, Ms. Manju Verma',
        'Dr. Laxmi Kant Sagar, Dr. Manmohan Singh Yadav, Dr. Neha Agrawal, Dr. Sandeep Kumar, Dr. Shikha Verma, Dr. Zatin Gupta, Dr. Yojna Arora, Mr. Ajai Verma, Mr. Amit Sharma, Mr. Nishant Upadhyay, Mr. Shashi Kant, Ms. Deepti Sahu, Ms. Namita Sharma',
        'Dr. Renu Mishra, Dr. Subrata Sahana, Dr. Sudeep Varshney, Dr. Vishal Jain, Dr. Anubhava Srivastava, Dr. Bal Saraswat, Dr. Bharat Bhushan, Dr. Ganesh Gupta, Dr. Krishan Kumar, Dr. Shelja Sharma, Mr. Amit Kumar Rai, Mr. Amit Sharma, Mr. Kandarp Narayan Mishra, Mr. Lalit Mohan, Mr. Rajiv Nath, Ms. Annu Mishra, Ms. Saurabhi, Ms. Sheenam Naaz',
        'Dr. Amrit Suman, Mr. Amrit Sharda, Mr. Amrit Singh - Sharda Informatics, Mr. Sandeep Sharda - Sharda Informatics, Mr. Sushant Jhingran, Mr. Tapas Kumar Mishra, Mr. Tapas Kumar Mishra / Mr. Girish Karwasara, Ms. Gunjan Aggarwal, Ms. Kanika Singla',
        'Dr. Ali Imam Abidi, Dr. Bhawna Mallick, Dr. Gaurav Raj, Dr. Javed Ahmad, Dr. Kalicharan, Dr. Neha Agrawal, Dr. Shikha Verma, Dr. Shipra Shukla / Ms. Manju Verma, Dr. Sonia Setia, Mr. Ashish Jain, Mr. Bal Saraswat, Mr. Himanshu Sharma, Mr. Kandarp Narayan Mishra, Mr. Mohammad Asim, Ms. Amita Sharma, Ms. Rosey Chauhan',
        'Ms. Lisha Yugal, Dr. Anjali, Dr. Rani Astya, Mr. Prashant Upadhyay, Prof. Vasudha Arora, Mr. Murari Kumar Singh, Mr. Amit Bhola, Mr. Himanshu Pandey, Mr. Jitendra Singh, Mr. Nishant Upadhyay, Mr. Pankaj Sharma, Dr. Saurabh Kumar',
        'Dr. Dharmendra Kumar, Ms. Ashu Goyal, Ms. Kamini, Mr. Durgesh Kumar, Mr. Mohammad Asim, Mr. Prem Prakash Aggarwal, Mr. Shashi Kant, Ms. Saurabhi Chaudhary, Prof. Shajee Mohan B. S., Dr. Sonia Setia, Ms. Teena Verma, Mr. Ashish Kumar',
        'Ms. Ashu Goyal, Mr. Shashi Kant, Mr. Anuj Gupta',
        'Dr. Vibha Thakur',
        'Dr. Ramneet, Dr. G. S. Mishra',
        'Dr. Krishan Kumar, Dr. Anubhav Shrivastav, Dr. Ashish Chakraverti, Mr. Nikhil Ranjan, Dr. Subrata Sahana, Mr. Nishant Upadhyay, Prof. Shajee Mohan B. S., Prof. Anil Kumar Sagar, Dr. Bharat Bhushan, Dr. Vishal Jain, Dr. Ramneet, Ms. Rosey Chauhan',
        'Ms. Priyanka Tiwari, Dr. Bharat Bhushan, Ms. Rosey Jadon, Mr. Ashish Kumar, Mr. Amit Kumar Rai',
        'Mr. Dharm Raj, Dr. Sandeep Kumar, Ms. Aanchal Vij, Mr. Prem Prakash Agrawal, Ms. Lisha Yugal, Mr. Kapil Kumar',
        'Dr. Mayank Goel',
        'Mr. Durgesh Kumar',
        'Dr. Rani Astya, Dr. Keshav Gupta, Mr. Bal Saraswat, Dr. Zatin Gupta, Mr. Kandarp Narayan',
        'Dr. Keshav Gupta'
    ],
    'Total Students': [60, 58, 55, 57, 61, 59, 53, 54, 51, 49, 50, 52, 47, 46, 48, 45, 44, 43],
    'Slow Learners': [15, 13, 11, 12, 14, 13, 10, 9, 8, 7, 8, 7, 6, 5, 7, 6, 5, 4],
    'Average Attendance %': [85, 87, 82, 83, 86, 88, 84, 80, 79, 78, 76, 75, 83, 81, 78, 77, 80, 79],
    'Quiz Completion %': [75, 77, 70, 71, 73, 74, 78, 76, 72, 73, 71, 72, 76, 77, 75, 74, 78, 77],
    'Assignment Completion %': [78, 79, 74, 76, 78, 77, 79, 78, 75, 73, 72, 71, 76, 74, 75, 74, 72, 73]
}
df = pd.DataFrame(data)

# Dropdown options for coordinators
coordinator_options = [{'label': coord, 'value': coord} for coord in df['Coordinator'].unique()]

# App Layout
app.layout = html.Div([
    html.H1("Enhanced Academic Dashboard with Faculty & Subject Details"),
    
    # Tabs for organized sections
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Executive Overview', value='tab-1'),
        dcc.Tab(label='Department Insights', value='tab-2'),
        dcc.Tab(label='Faculty Impact', value='tab-3'),
    ]),
    html.Div(id='tabs-content')
])

# Dynamic content callback for tabs
@app.callback(Output('tabs-content', 'children'), Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        fig_total_students = px.bar(df, x='Coordinator', y='Total Students', title="Total Students by Coordinator")
        fig_slow_learners = px.bar(df, x='Coordinator', y='Slow Learners', title="Slow Learners by Coordinator")
        return html.Div([
            html.H3("Executive Overview"),
                        dcc.Graph(figure=fig_total_students),
            dcc.Graph(figure=fig_slow_learners)
        ])
    
    elif tab == 'tab-2':
        fig_dept_slow_learners = px.bar(df, x='Coordinator', y='Slow Learners', color='Coordinator', title="Slow Learners by Department")
        return html.Div([
            html.H3("Departmental Insights"),
            dcc.Graph(figure=fig_dept_slow_learners)
        ])
    
    elif tab == 'tab-3':
        return html.Div([
            html.H3("Faculty Impact Analysis"),
            dcc.Dropdown(id='coordinator-filter', options=coordinator_options, placeholder="Select Coordinator"),
            dcc.Dropdown(id='subject-filter', placeholder="Select Subject"),
            html.Div(id='faculty-impact-content')
        ])

# Callback to update subjects based on selected coordinator
@app.callback(
    Output('subject-filter', 'options'),
    Input('coordinator-filter', 'value')
)
def update_subject_options(selected_coordinator):
    if selected_coordinator:
        subjects = df[df['Coordinator'] == selected_coordinator]['Subject'].unique()
        return [{'label': subject, 'value': subject} for subject in subjects]
    return []

# Callback for Faculty Impact based on selected subject
@app.callback(
    Output('faculty-impact-content', 'children'),
    [Input('coordinator-filter', 'value'), Input('subject-filter', 'value')]
)
def update_faculty_impact(selected_coordinator, selected_subject):
    if not selected_coordinator or not selected_subject:
        return html.Div("Please select both Coordinator and Subject to view Faculty Impact.")

    filtered_df = df[(df['Coordinator'] == selected_coordinator) & (df['Subject'] == selected_subject)]
    
    if filtered_df.empty:
        return html.Div("No data available for the selected Coordinator and Subject.")
    
    fig_faculty_slow_learners = px.bar(
        filtered_df, x='Faculty', y='Slow Learners',
        title=f"Slow Learners per Faculty for {selected_subject}"
    )
    
    fig_attendance_completion = go.Figure()
    fig_attendance_completion.add_trace(go.Bar(
        x=filtered_df['Faculty'],
        y=filtered_df['Average Attendance %'],
        name="Average Attendance %"
    ))
    fig_attendance_completion.add_trace(go.Bar(
        x=filtered_df['Faculty'],
        y=filtered_df['Quiz Completion %'],
        name="Quiz Completion %"
    ))
    fig_attendance_completion.add_trace(go.Bar(
        x=filtered_df['Faculty'],
        y=filtered_df['Assignment Completion %'],
        name="Assignment Completion %"
    ))
    fig_attendance_completion.update_layout(
        title=f"Engagement Metrics for {selected_subject}",
        barmode='group'
    )

    return html.Div([
        dcc.Graph(figure=fig_faculty_slow_learners),
        dcc.Graph(figure=fig_attendance_completion)
    ])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
