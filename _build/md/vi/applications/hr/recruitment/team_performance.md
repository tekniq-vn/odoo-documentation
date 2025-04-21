# Team performance reporting

The *Team Performance* report in the **Recruitment** app shows how many applicants each recruiter is
managing.

This information is determined by the individuals populating the [Recruiter](add-new-applicants.md#recruitment-applicant-details) field on each applicant form.

## Open report

To access the *Team Performance* report, navigate to Recruitment app ‣ Reporting
‣ Team Performance.

The number of In Progress, Hired, and Refused applicants for
each recruiter is displayed in the <i class="fa fa-area-chart"></i> (Graph) view.

The information shown is for the <i class="fa fa-filter"></i> Last 365 Days Applicant default
filter, as displayed in the search bar.

Hover the cursor over any column to view a popover window, displaying the specific details for that
column.

![The default bar chart of the team performance report.](applications/hr/recruitment/team_performance/team-performance.png)

### Pivot table view

For a more detailed view of the information in the Team Performance report, click the
<i class="oi oi-view-pivot"></i> (Pivot) icon in the top-right corner. This displays all the
information in a pivot table.

In this view, the job positions are displayed in the rows, while the columns display the total
number of applicants. The applicants are further organized by # Applicant (in process),
# Hired, and # Refused.

The displayed information can be modified, if desired.

In this example, there are 19 total applicants. Out of those 19, eight have been hired, and three
refused.

From the data presented, the Experienced Developer job position is the most successful.
This job position has the highest number of total applicants, as well as the most hires. In
addition, the Experienced Developer has the least amount of refused applicants.

This pivot table also shows that the Chief Executive Officer position is the hardest to
fill, as it has the fewest total applicants.

![The detailed pivot table view.](applications/hr/recruitment/team_performance/team-perf-pivot.png)

## Use case: recruiter performance over time

One way to modify this report is to show how recruiters are performing over time. To show this
information, begin with the Team Performance report in the <i class="oi oi-view-pivot"></i>
(Pivot) view.

Next, click the <i class="fa fa-caret-down"></i> (down arrow) in the search bar, revealing a
drop-down menu. Click Add Custom Group <i class="oi oi-caret-down"></i> at the bottom of the
<i class="oi oi-group"></i> Group By column, then click Recruiter. Click away from the
drop-down menu to close it. Now, each row on the table represents a recruiter.

![The pivot table now displaying the recruiters in the rows.](applications/hr/recruitment/team_performance/by-recruiter.png)

To compare the team's performance over different time periods, click the <i class="fa fa-caret-down"></i>
(down arrow) in the search bar. Click Start Date <i class="fa fa-caret-down"></i> in
the <i class="fa fa-filter"></i> Filters column, revealing various time periods to select.

In this example, the desired data is the comparison between the team's performance in the third
quarter (June - August) and the second quarter (April - July). To do so, click Q3. Once
clicked, the current year is also ticked. In this example, it is 2024.

After making this selection, a <i class="fa fa-adjust"></i> Comparison column appears. Click
Start Date: Previous Period to compare the third quarter with the second quarter, for
the various recruiters.

![A comparison table of recruiter totals of Q2 and Q3.](applications/hr/recruitment/team_performance/compare.png)

From this report, several things can be extrapolated: the total number of applicants increased, the
number of hired applicants remained the same, while the number of refused applicants decreased.

Additionally, Jane Jobs had the highest increase in number of applicants during the
third quarter, but her number of hired applicants went down 67%. The recruiter with the
best overall numbers was Rose Recruiter, who had both their active applicants and hired
applicants, increase in the third quarter, while their refused applicants went down.
