# Recruitment flow

When a prospective employee applies for a job in Odoo, there is a preconfigured process from the
[initial inquiry](#recruitment-new) to the [creating of a new employee](offer_job_positions.md#recruitment-new-employee) once hired. The following outlines the default recruitment process for
Odoo's *Recruitment* application.

#### IMPORTANT
The following is based on Odoo's default recruitment pipeline. Be advised that if
[modifications are made](../recruitment.md#recruitment-customize-stages) to the pipeline, the process
differs.

<a id="recruitment-new"></a>

## Mới

At the start of the process, all applicants appear in the New stage on the
Applications page, whether submitted online or if the applicant is [manually
entered by a recruiter](add-new-applicants.md).

When the applicant's card is created, Odoo automatically populates the
Subject/Application, the Applicant's Name, Email, and
Mobile number, on the applicant's card. This information is required when applying for
a job position, by default.

#### NOTE
If the website application form is modified, different fields may be populated, based on what
information is requested on the website.

If the applicant entered any information in the *Short Introduction* section of the online
application, it populates the Application Summary tab at the bottom of the applicant's
card.

### Resumé

If a resumé was attached to the online application, it appears in the Files section of
the chatter, and is also stored in the *Documents* application.

To find the recruitment documents, navigate to the main Documents app dashboard,
and click the Recruitment folder on the left-hand side. All recruitment documents are
stored within that folder.

If the [CV Display](../recruitment.md#recruitment-cv-display) option was enabled in the [Settings](../recruitment.md#recruitment-settings) of the *Recruitment* app, the resumé appears on the applicant's card, on the
right-hand side.

#### NOTE
Depending on the browser zoom level, or size of the browser screen, the resumé may appear below
the main applicant card information as a PDF link.

### Send interview

At any point in the hiring process, an interview can be sent to the applicant to obtain more
information. These interviews are custom-made, and can be formatted in a variety of ways.

The *Surveys* application is **required** to send interviews to an applicant, so it **must** be
installed.

Odoo uses the term *interview*, but these can be thought of as questionnaires, surveys, tests,
certifications, etc. Custom interviews can be formatted to suit each individual job position's
needs. For more information on creating and editing interviews, refer to the
[Job positions](new_job.md) documentation.

To send an interview to an applicant, first click the applicant's card from the
Applications page, to view the detailed applicant information. At the top-left of the
applicant's card, click the Send Interview button.

If the applicant's card has an email address on file, a Send an interview pop-up window
appears, with the Recipients, Subject, and email body populated.

#### NOTE
To send an email to an applicant, there **must** be an Email address on the
applicant's card.

If an email address is not entered on the applicant's card, when the Send Interview
button is clicked, an Edit: (Applicant's Name) pop-up window appears, *on top of* the
Send an interview pop-up window.

Enter the email address in the Email field, then click Save & Close.

Once the applicant's information is saved, the Edit: (Applicant's Name) pop-up window
closes, and the Send an interview pop-up window remains.

Đôi khi, các mẫu email được cấu hình sẵn trong Odoo sử dụng các phần giữ chỗ động, sẽ tự động được điền bằng dữ liệu cụ thể khi email được gửi. Ví dụ, nếu một trình giữ chỗ dành cho tên ứng viên được sử dụng, nó sẽ được thay thế bằng tên thực tế của ứng viên trong email. Để biết thêm thông tin chi tiết về mẫu email, hãy tham khảo tài liệu [Mẫu Email](../../general/companies/email_template.md).

Thêm địa chỉ email của bất kỳ người nhận bổ sung nào cho khảo sát vào trường Email bổ sung, nếu muốn thêm người nhận email. Nếu một địa chỉ email có trong cơ sở dữ liệu dưới dạng liên hệ, hãy thêm liên hệ đó vào trường Người nhận. Nếu một email cần được gửi đến một người không có trong cơ sở dữ liệu dưới dạng liên hệ và họ **không** nên được thêm vào làm liên hệ, hãy thêm địa chỉ email của họ vào trường Email bổ sung.

If any attachments need to be added, click the <i class="fa fa-paperclip"></i> Attachments button,
and a file explorer window appears. Navigate to the desired file, and click Open to
attach it to the email. The attachment loads, and is listed above the <i class="fa fa-paperclip"></i>
Attachments button.

If the emailed interview must be completed by a specific date, enter that date in the
Answer deadline field, located in the lower-right area of the pop-up window.

To do so, click the empty field next to Answer deadline, and a calendar selector
appears. Use the <i class="fa fa-chevron-left"></i> (left) and <i class="fa fa-chevron-right"></i>
(right) arrows, on either side of the month, to navigate to the desired month. Then,
click on the desired day to select the date.

The Mail Template field is pre-populated, based on the configuration for the interview.
A different template can be chosen from the drop-down menu, if desired. If a new template is
selected, the new email template loads in the email body.

To send the email with the interview link to the applicant, click Send at the bottom of
the email pop-up window.

![Send a custom survey, also referred to as an interview form, to an applicant using a
pre-configured template.](applications/hr/recruitment/recruitment-flow/send-survey.png)

<a id="recruitment-initial-qualification"></a>

## Initial qualification

If an applicant seems to be a good potential candidate, they are moved to the Initial
Qualification stage.

This stage exists to quickly sort candidates that have potential, from those that do not meet the
requirements. No automatic actions, such as emails, are set for this stage. This stage simply
informs the recruitment team to potentially set up a phone call or an interview with the candidate.

#### NOTE
> In order to move an applicant's card from one stage to another, the applicant's card can either
> be dragged and dropped in the Kanban view of the Applications page to the desired
> stage, or the stage can be modified on the applicant's card.

> To change the stage on the applicant's card, first click the desired applicant's card from the
> Applications page. The current stage for the card is highlighted at the top on a
> status bar, above the card.

> Click the desired stage for the card, and the stage changes. A log note indicating the stage
> change appears in the chatter, as well.
![Change the stage of an applicant by clicking on the desired stage at the top of the
applicant's card.](applications/hr/recruitment/recruitment-flow/stage-change.png)

<a id="recruitment-first-interview"></a>

## First interview

After an applicant has passed the Initial Qualification stage, they can be manually
moved to the First Interview stage on the Applications page, while in Kanban
view.

To move the applicant to the next stage, drag-and-drop the applicant's card to the First
Interview stage.

Alternatively, open the desired applicant's card from the Applications page, and click
the First Interview stage on the status bar at the top of the individual applicant's
card.

![An applicant's card moves from one stage to another by using the click and drag method.](applications/hr/recruitment/recruitment-flow/move.png)

<a id="recruitment-second-interview"></a>

## Second interview

Sau khi ứng viên vượt qua giai đoạn Phỏng vấn lần 1, họ có thể được chuyển sang giai đoạn Phỏng vấn lần 2. Để chuyển ứng viên sang giai đoạn tiếp theo, kéo-thả thẻ ứng viên vào cột Phỏng vấn lần 2 từ chế độ xem Kanban của trang Đơn ứng tuyển, hoặc nhấp vào giai đoạn Phỏng vấn lần 2 ở đầu thẻ của mỗi ứng viên.

When the applicant's card moves to the Second Interview stage, there are no automatic
activities or emails configured for this stage, by default. The recruiter can now [schedule a
second interview](schedule_interviews.md#recruitment-schedule-interviews-recruitment-scheduled) with the applicant,
following the same process as the first interview.

<a id="recruitment-contract-proposal"></a>

## Đề xuất Hợp đồng

After the applicant has completed the various interview processes, the next step is to [send
the job offer](offer_job_positions.md).

Once the offer has been sent, drag-and-drop the applicant's card to the Contract
Proposal stage from the Kanban view of the Applications page, or click on the
Contract Proposal stage at the top of the individual applicant's card.

## Hợp đồng được ký

Once the contract has been signed, and the applicant has been hired, the applicant's card moves to
the Contract Signed stage.

Drag-and-drop the applicant's card to the Contract Signed stage from the Kanban view of
the Applications page, or click the <i class="fa fa-ellipsis-h"></i> (ellipsis) icon at
the top of the individual applicant's card, then click Contract Signed on the status
bar.

## Refuse applicant

At any point in the recruitment process, a candidate can be [refused](refuse_applicant.md).
