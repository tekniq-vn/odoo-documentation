# Báo cáo

Odoo *Live Chat* includes several reports that allow for the monitoring of operator performance and
the identification of trends in customer conversations.

## Available reports

The following reports are included in the *Live Chat* app:

- [Sessions History](#livechat-sessions-history)
- [Session Statistics](#livechat-session-statistics)
- [Operator Analysis](#livechat-operator-analysis)

#### NOTE
The *Live Chat Ratings Report* can also be accessed through the Report menu. For more
information on this report, and on the *Live Chat* rating process, see [Live Chat Ratings](ratings.md).

To access a drop-down menu of all the available reports, navigate to Live Chat app
‣ Report.

<a id="livechat-sessions-history"></a>

### Lịch sử Phiên

The *Sessions History* report displays an overview of live chat sessions, including session dates,
participant name and country, session duration, the number of messages, and the rating. It also
provides access to the complete transcripts of live chat sessions.

To access this report, navigate to Live Chat app ‣ Report ‣ Sessions History.

![Example of the Sessions History report from the Live Chat application.](applications/websites/livechat/reports/sessions-history.png)

The information in this report can be exported, or inserted into a spreadsheet.

Click the ⚙️ (gear) icon to the right of the History page title, in the
top-left corner. Doing so reveals a drop-down menu.

From the drop-down menu, click Export All to export all sessions to a spreadsheet, or
Insert list in spreadsheet to insert the information in a new, or existing, spreadsheet.

To only export select sessions, first select the desired sessions to be exported from the list, by
clicking the checkbox to the left of each individual session. With the sessions selected, click the
⚙️ (gear) Actions icon in the top-center of the page, and click Export or
Insert list in spreadsheet.

To view the transcript of an individual conversation, click anywhere on the entry line. This opens
the *Discuss* thread for the conversation.

In the *Discuss* thread, the conversation view displays the entire transcript of the conversation.
At the top of the conversation, there is a list of the web pages the visitor browsed before
beginning their chat session, along with corresponding time stamps. If the visitor left a rating, it
is included at the end of the transcript.

![View of the chat transcript in the Discuss application.](applications/websites/livechat/reports/chat-transcript.png)

<a id="livechat-session-statistics"></a>

### Session Statistics

The *Session Statistics* report provides a statistical overview of live chat sessions. The default
view for this report displays sessions grouped by the date of creation.

To access this report, navigate to Live Chat app ‣ Reports ‣ Session
Statistics.

![Example of the Sessions Statistics report from the Live Chat application.](applications/websites/livechat/reports/sessions-statistics.png)

To view a different measure, click the Measures drop-down menu at the top-left of the
report. The measures available for this report include:

- # of speakers: number of participants in the conversation.
- Days of activity: number of days since the operator's first session.
- Duration of Session (min): the duration of a conversation, in minutes.
- Is visitor anonymous: denotes whether the conversation participant is anonymous.
- Messages per session: the total number of messages sent in a conversation. This
  measure is included in the default view.
- Rating: the rating received by an operator at the end of a session, if one was
  provided.
- Session not rated: denotes if a session did **not** receive a rating at the end of the
  conversation.
- Time to answer (sec): the average time, in seconds, before an operator responds to a
  chat request.
- Visitor is Happy: denotes whether a positive rating was provided. If the visitor gave
  either a negative or neutral rating, they are considered *unhappy*.
- Count: the total number of sessions.

<a id="livechat-operator-analysis"></a>

### Phân tích người đại diện

The *Operator Analysis* report is used to monitor the performance of individual live chat operators.

To access the report, navigate to Live Chat app ‣ Reports ‣ Operator Analysis.

The default view for this report is a bar chart, which only displays conversations from the current
month, as indicated by the This Month default search filter. Conversations are grouped
by operator.

To view a different measure, click the Measures drop-down menu at the top-left of the
report. The measures available for this report include:

- # of Sessions: the number of sessions an operator participated in. This measure is
  included by default.
- Average duration: the average duration of a conversation, in seconds.
- Average rating: the average rating received by the operator.
- Time to answer: the average amount of time before the operator responds to a chat
  request, in seconds.
- Count: the total number of sessions.

![Example of the Operator Analysis report from the Live Chat application.](applications/websites/livechat/reports/operator-analysis.png)

## View and filter options

On any Odoo report, the view and filter options vary, depending on what data is being analyzed,
measured, and grouped. See below for additional information on the available views for the *Live
Chat* reports.

#### NOTE
The [Sessions History](#livechat-sessions-history) report is **only** available in list
view.

### Chế độ xem pivot

The *pivot* view presents data in an interactive manner. The [Session Statistics](#livechat-session-statistics) and [Operator Analysis](#livechat-operator-analysis) reports are
available in pivot view.

The pivot view can be accessed on a report by selecting the grid icon at the top-right
of the screen.

To add a group to a row or column, click the ➕ (plus sign) icon next to
Total, and then select one of the groups from the drop-down menu that appears. To remove
one, click the ➖ (minus sign) icon, and de-select the appropriate option.

### Chế độ xem biểu đồ

The *graph* view presents data in either a *bar*, *line*, or *pie* chart. The [Session
Statistics](#livechat-session-statistics) and [Operator Analysis](#livechat-operator-analysis)
reports are available in graph view.

Switch to the graph view by selecting the line chart icon at the top-right of the
screen. To switch between the different charts, select the desired view's corresponding icon at the
top-left of the chart, while in graph view.

### Save and share a favorite search

The *Favorites* feature found on reports allows users to save their most commonly used filters,
without having to reconstruct them every time they are needed.

To create and save a filter to the *Favorites* section on the search bar drop-down menu, follow the
steps below:

1. Set the necessary parameters using the Filters and Group By options
   available in the Search... bar drop-down menu and the Measures drop-down
   menu at the top-left of the report.
2. Click the 🔻(triangle pointed down) icon next to the Search... bar to
   open the drop-down menu.
3. Under the Favorites heading, click Save current search.
4. Rename the search.
5. Select Default filter to have these filter settings automatically displayed when the
   report is opened. Otherwise, leave it blank.
6. Select Shared to make this filter available to all other database users. If this box
   is not checked, the filter is only available to the user who creates it.
7. Click Save to preserve the configuration for future use.
