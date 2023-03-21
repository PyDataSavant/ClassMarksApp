import pandas as pd
import streamlit as st

df = pd.read_csv('marks_cleaned_data.csv')

st.sidebar.title('Students Marks Analysis')

option = st.sidebar.selectbox('Select Any One', ['Merit List', 'Eng Toppers', 'Math Toppers', 'TOP5 Students',
                                                 '80% above students', 'Class Average Marks',
                                                 'Students with more than AVG Marks',
                                                 'Extra Curricular Activities'])


# 1.Show merit list
if option == 'Merit List':
    btn = st.sidebar.button('Find Details')
    if btn:
        merit_list_df = df.sort_values(by='percentage', ascending=False, ignore_index=True)
        st.title('Bar graph showing students with highest percentage at top')
        st.write('Visualized Data')
        st.bar_chart(merit_list_df, x='name', y='percentage', use_container_width=True)
        st.write('Textual Data: Highest percentage at top and lowest at bottom')
        st.write(merit_list_df)


# 2.Show top5 score in English
elif option == 'Eng Toppers':
    btn = st.sidebar.button('Find Details')
    if btn:
        eng_top5_toppers_df = df[['roll_num', 'name', 'eng']].sort_values(by='eng', ascending=False,
                                                                          ignore_index=True).head(5)

        st.title('Bar graph showing students with highest marks in English at top')
        st.write('Visualized Data')
        st.bar_chart(eng_top5_toppers_df, x='name', y='eng', use_container_width=True)
        st.write('Textual Data')
        st.write(eng_top5_toppers_df)

# 3.Show top5 score in Math
elif option == 'Math Toppers':
    btn = st.sidebar.button('Find Details')
    if btn:
        math_top5_toppers_df = df[['roll_num', 'name', 'math']].sort_values(by='math', ascending=False,
                                                                            ignore_index=True).head(5)

        st.title('Bar graph showing students with highest marks in Math at top')
        st.write('Visualized Data')
        st.bar_chart(math_top5_toppers_df, x='name', y='math', use_container_width=True)
        st.write('Textual Data')
        st.write(math_top5_toppers_df)

# 4.Show top5 students of the class
elif option == 'TOP5 Students':
    btn = st.sidebar.button('Find Details')
    if btn:
        top5_students_df = df.sort_values(by='percentage', ascending=False, ignore_index=True).head(5)

        st.title('Bar graph showing top5 students of the class')
        st.write('Visualized Data')
        st.bar_chart(top5_students_df, x='name', y='percentage', use_container_width=True)
        st.write('Textual Data')
        st.write(top5_students_df)

# 5. Show students with more than 80%
elif option == '80% above students':
    btn = st.sidebar.button('Find Details')
    if btn:
        more_than_eighty_pct_df = df[df['percentage'] > 80].sort_values(by='percentage', ascending=False,
                                                                        ignore_index=True)

        st.title('Bar graph showing students with more than 80% marks overall')
        st.write('Visualized Data')
        st.bar_chart(more_than_eighty_pct_df, x='name', y='percentage', use_container_width=True)
        st.write('Textual Data')
        st.write(more_than_eighty_pct_df)

# 6.Show average marks of the class
elif option == 'Class Average Marks':
    btn = st.sidebar.button('Find Details')
    if btn:
        avg_df = df['percentage'].mean()

        st.title('Data shows Average marks of the class')
        st.write('Textual Data')
        st.write(avg_df)

# 7.Show students with more than average value
elif option == 'Students with more than Class AVG Marks':
    btn = st.sidebar.button('Find Details')
    if btn:
        avg_df = df['percentage'].mean()
        more_than_avg_df = df[df['percentage'] > avg_df].sort_values(by='percentage', ascending=False,
                                                                     ignore_index=True)

        st.title('Bar graph showing students with more than average marks')
        st.write('Visualized Data')
        st.bar_chart(more_than_avg_df, x='name', y='percentage', use_container_width=True)
        st.write('Textual Data')
        st.write(more_than_avg_df)

# 8.Top5 students who are experts in extra curricular activities
elif option == 'Extra Curricular Activities':
    btn = st.sidebar.button('Find Details')
    if btn:
        df1 = df.copy()
        df2 = df1[['name', 'drawing', 'rhymes']]
        df2['ext_cur'] = df2['drawing'] + df2['rhymes']
        df3 = pd.merge(df1, df2, how='left', left_on=['name', 'drawing', 'rhymes'],
                       right_on=['name', 'drawing', 'rhymes'])
        df_final = df3[
            ['roll_num', 'name', 'hindi_w', 'hindi_o', 'hindi', 'eng_w', 'eng_o', 'eng', 'math_w', 'math_o', 'math',
             'gk_o', 'drawing', 'rhymes', 'ext_cur', 'marks_secured', 'percentage']]
        ext_cur_df = df_final.sort_values(by='ext_cur', ascending=False, ignore_index=True).head(5)[
            ['roll_num', 'name', 'drawing', 'rhymes', 'ext_cur']]

        st.title('Bar graph showing students with more marks in drawings and rhymes')
        st.write('Visualized Data')
        st.bar_chart(ext_cur_df, x='name', y='ext_cur', use_container_width=True)
        st.write('Textual Data')
        st.write(ext_cur_df)
