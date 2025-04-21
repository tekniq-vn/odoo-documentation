# Học trực tuyến

The **eLearning** app allows you to easily upload content, define learning objectives, manage
attendees, assess students' progress, and even set up rewards. Engaging participants in a meaningful
learning experience enhances their attentiveness and fosters heightened productivity.

#### IMPORTANT
You can manage your eLearning content on the **front end** or the **back end**. The **front end**
allows you to create content quickly from your website, while the **back end** provides
additional options and allows collaboration. This documentation focuses on using the back end to
create your content.

#### SEE ALSO
[Odoo Tutorials: eLearning](https://www.odoo.com/slides/elearning-56)

## Khóa học

By going to eLearning ‣ Courses ‣ Courses, you can get an overview of all your
courses.

Click on a course title to edit your course on the back end. Click on View course to
access your course on the front end.

### Course creation

Nhấp Mới để tạo khóa học mới. Khi trang hiện ra, bạn có thể thêm Tiêu đề khóa học và một hoặc nhiều Thẻ để mô tả khóa học. Bạn có thể thêm hình ảnh minh họa bằng cách di chuột vào hình ảnh camera giữ chỗ và nhấp vào biểu tượng chỉnh sửa. Bốn tab cho phép bạn chỉnh sửa thêm khóa học: [Nội dung](#elearning-content), [Mô tả](#elearning-description), [Tùy chọn](#elearning-options) và [Karma](#elearning-karma).

![Create your elearning course.](elearning/elearning-course-creation.png)

<a id="elearning-content"></a>

#### Content tab

This tab allows you to manage your course content. Click on Add Section to divide your
course into different sections. Click on Add Content to create
[content](#elearning-create-content). Click on Add Certification to assess the
level of understanding of your attendees, certify their skills, and motivate them. **Certification**
is part of the [Surveys](../marketing/surveys/create.md) app.

<a id="elearning-description"></a>

#### Tab mô tả

You can add a short description or information related to your course in the Description
tab. It appears under your course title on your website.

![Add a description to your course.](elearning/course-description.png)

<a id="elearning-options"></a>

#### Options tab

In the Options tab, different configurations are available:
[Course](#elearning-course),  [Communication](#elearning-communication),
[Access rights](#elearning-access-rights), and [Display](#elearning-display).

![Overview of the Options tab](elearning/options-tab.png)

<a id="elearning-course"></a>

##### Khóa học

Assign a Responsible user for your course. If you have multiple websites, use the
Website field to only display the course on the selected website.

<a id="elearning-communication"></a>

##### Thông tin trao đổi

- Allow Reviews: tick the box to allow attendees to like and comment on your content and
  to submit reviews on your course;
- Forum: add a dedicated forum to your course (only shown if the **Forum** feature is
  enabled in the app's settings);
- New Content Notification: select an email template sent to your attendees when you
  upload new content. Click on the internal link button (➜) to have access to the email
  template editor;
- Completion Notification: select an email template sent to your attendees once they
  reach the end of your course. Click on the internal link button (➜) to access the
  email template editor;

<a id="elearning-access-rights"></a>

##### Quyền truy cập

- Prerequisites: set one or more courses that users are advised to complete before
  : accessing your course;
- Show course to: define who can access your course and their content between
  Everyone, Signed In or Course Attendees;
- Enroll Policy: define how people enroll in your course. Select:
  > - Open: if you want your course to be available to anyone;
  > - On Invitation: if only people who received an invitation can enroll to your course.
  >   If selected, fill in the Enroll Message explaining the course's enrollment process.
  >   This message appears on your website under the course title;
  > - On Payment: if only people who bought your course can attend it. The
  >   Paid Courses feature must be enabled to get this option. If you select
  >   On Payment, you must add a Product for your course.
  >   > #### NOTE
  >   > Only products set up with Course as their Product Type are
  >   > displayed.

<a id="elearning-display"></a>

##### Hiển thị

- Training: the course content appears as a training program, and the courses must be
  taken in the proposed order.
- Documentation: the content is available in any order. If you choose this option, you
  can choose which page should be promoted on the course homepage by using the
  Featured Content field.

<a id="elearning-karma"></a>

#### Karma tab

This tab is about gamification to make eLearning fun and interactive.

In the Rewards section, choose how many karma points you want to grant your students
when they Review or Finish a course.

In the Access Rights section, define the karma needed to Add Review,
Add Comment, or Vote on the course.

#### NOTE
From your course, click the Contact Attendees button to reach people who are
enrolled in the course.

<a id="elearning-course-groups"></a>

### Course groups

Use the **Course Groups** to inform users and allow them to filter the courses from the
All Courses dashboard.

You can manage them by going to Configuration ‣
Course Groups. Click New to create a new course group. Add the Course Group
Name, tick the Menu Entry box to allow users to search by course group on the website,
and add tags in the Tag Name column. For each tag, you can select a corresponding color.

### Cài đặt

You can enable different features to customize your courses by going to eLearning
‣ Configuration ‣ Settings:

- **Certifications**: to evaluate the knowledge of your attendees and certify their skills;
- **Paid courses**: to sell access to your courses on your website and track revenues;
- **Mailing**: to update all your attendees at once through mass mailings;
- **Forum**: to create a community and let attendees answer each other's questions.

<a id="elearning-create-content"></a>

## Nội dung

Manage your content by going to eLearning ‣ Courses ‣ Contents. Click
New to create content. Add your Content Title, and if you want
[Tags](#elearning-tags), then fill in the related information among the different tabs.

![Create your content.](elearning/elearning-content-tab.png)

### Document tab

- Course: select the course your content belongs to;
- Content Type: select the type of your content;
- Responsible: add a responsible person for your content;
- Duration: indicate the time required to complete the course;
- Allow Download: allow users to download the content of the slide. This option is only
  visible when the content is a document;
- Allow Preview: the course is accessible by anyone.
- # of Public Views: displays the number of views from non-enrolled participants;
- # Total Views: displays the total number of views (non-enrolled and enrolled
  participants).

### Tab mô tả

You can add a description of your content that appears front end in the About section of
your course content.

### Additional Resources tab

Click Add a line to add a link or a file that supports your participants' learning.
It appears in the course content on your website.

![Additional ressources](elearning/additional-content.png)

<a id="elearning-quiz"></a>

### Tab quiz

From this tab you can create a quiz to assess your students at the end of the course.

Phần Điểm thưởng cho phép bạn đưa ra một số điểm karma cụ thể tùy vào số lần cần để trả lời đúng câu hỏi. Sau đó, tạo câu hỏi và các câu trả lời có thể bằng cách nhấp vào Thêm một dòng. Một cửa sổ mới sẽ bật lên, thêm câu hỏi bằng cách điền vào Tên câu hỏi và thêm nhiều câu trả lời bằng cách nhấp vào Thêm một dòng. Chọn Là câu trả lời đúng để đánh dấu một hoặc nhiều câu trả lời là đúng. Bạn cũng có thể điền vào trường Bình luận để hiển thị thông tin bổ sung khi người tham gia chọn câu trả lời.

<a id="elearning-tags"></a>

### Từ khóa nội dung

The **Content Tags** help users to classify the content from the Contents dashboard.

You can manage them by going to eLearning ‣ Configuration ‣ Content Tags. Click
New to create a new tag.

## Publish your content

Everything created on the back end needs to be published from the front end. Unpublished content is
always visible from your website but still needs to be published to be available to your audience.

You must be on your website's front end to publish your content. To do so, click on the
Go To Website smart button, and tick the Publish option available in the
right-hand corner.

![Publish your content.](elearning/elearning-publish-button.png)
