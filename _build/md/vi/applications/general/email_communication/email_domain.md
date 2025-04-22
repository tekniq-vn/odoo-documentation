# Configure DNS records to send emails in Odoo

This documentation presents three complementary authentication protocols (SPF, DKIM, and DMARC) used
to prove the legitimacy of an email sender. Not complying with these protocols will greatly reduce
chances of your emails to reach their destination.

**Odoo Online** and **Odoo.sh** databases using the **default Odoo subdomain address** (e.g.,
`@company-name.odoo.com`) are pre-configured to **send authenticated emails** compliant with the
SPF, DKIM, and DMARC protocols.

If choosing to use a **custom domain** instead, **configuring SPF and DKIM records correctly is
essential** to prevent emails from being quarantined as spam or not being delivered to recipients.

If using [the default Odoo email server to send emails from a custom domain](applications/general/email_communication/email_servers_outbound.md#email-outbound-custom-domain-odoo-server), the SPF and DKIM records must be configured as
presented below. If using an outgoing email server, it is required to use the SPF and DKIM records
specific to that email service and a custom domain.

#### NOTE
Email service providers apply different rules to incoming emails. An email may be classified as
spam even if it passes the SPF and DKIM checks.

<a id="email-domain-spf"></a>

## SPF (Sender Policy Framework)

Giao thức Khung chính sách người gửi (SPF) cho phép chủ sở hữu của một tên miền chỉ định những máy chủ nào được phép gửi email từ miền đó. Khi một máy chủ nhận được email đến, nó sẽ kiểm tra xem địa chỉ IP của máy chủ gửi có nằm trong danh sách các IP được phép theo bản ghi  hay không.

In Odoo, the **SPF test is performed on the bounce address** defined under the Alias
Domain field found under the database's General Settings. If using a custom domain as
Alias Domain, it is necessary to configure it to be SPF-compliant.

The SPF policy of a domain is set using a TXT record. The way to create or modify this record
depends on the provider hosting the  zone of the domain name.

If the domain name does not yet have an SPF record, create one using the following input:

```bash
v=spf1 include:_spf.odoo.com ~all
```

If the domain name **already has an SPF record, the record must be updated**. Do not create a new
one, as a domain must have only one SPF record.

Check the SPF record using a tool like [MXToolbox SPF Record Check](https://mxtoolbox.com/spf.aspx). The process to create or modify an SPF record depends on the
provider hosting the DNS zone of the domain name. The [most common providers](#email-domain-providers-documentation) and their documentation are listed below.

<a id="email-domain-dkim"></a>

## DKIM (DomainKeys Identified Mail)

The DomainKeys Identified Mail (DKIM) allows a user to authenticate emails with a digital signature.

Khi gửi email, máy chủ email của Odoo sẽ bao gồm một chữ ký :abbr:

```
`
```

DKIM (Giao thức xác minh email DomainKeys) duy nhất trong phần header. Máy chủ của người nhận sẽ giải mã chữ ký này bằng cách sử dụng bản ghi DKIM trong tên miền của cơ sở dữ liệu. Nếu chữ ký và khóa chứa trong bản ghi khớp nhau, điều này chứng minh rằng tin nhắn là xác thực và không bị thay đổi trong quá trình vận chuyển.

Enabling DKIM is **required** when sending emails **from a custom domain** using the Odoo email
server.

To enable DKIM, add a  record to the 
zone of the domain name:

```bash
odoo._domainkey IN CNAME odoo._domainkey.odoo.com.
```

The way to create or modify a CNAME record depends on the provider hosting the DNS zone of the
domain name. The [most common providers](#email-domain-providers-documentation) and their
documentation are listed below.

Check if the DKIM record is valid using a tool like [MXToolbox DKIM Record Lookup](https://mxtoolbox.com/dkim.aspx). Enter `example.com:odoo` in the DKIM lookup tool, specifying
that the selector being tested is `odoo` for the custom domain `example.com`.

<a id="email-domain-dmarc"></a>

## DMARC (Domain-based Message Authentication, Reporting and Conformance)

The  record is a
protocol that unifies  and . The instructions contained in the DMARC record of a domain name tell the destination server
what to do with an incoming email that fails the SPF and/or DKIM check.

#### NOTE
The aim of this documentation is to help **understand the impact DMARC has on the deliverability
of emails**, rather than give precise instructions for creating a DMARC record. Refer to a
resource like [DMARC.org](https://dmarc.org/) to set the DMARC record.

There are three DMARC policies:

- `p=none`
- `p=quarantine`
- `p=reject`

`p=quarantine` and `p=reject` instruct the server that receives an email to quarantine that email or
ignore it if the SPF or DKIM check fails.

#### NOTE
**For the DMARC to pass, the DKIM or SPF check needs to pass** and the domains must be in
alignment. If the hosting type is Odoo Online, DKIM configuration on the sending domain is
required to pass the DMARC.

Passing DMARC generally means that the email will be successfully delivered. However, it's important
to note that **other factors like spam filters can still reject or quarantine a message**.

`p=none` is used for the domain owner to receive reports about entities using their domain. It
should not impact the deliverability.

<a id="email-domain-mail-config-common-providers"></a>

<a id="email-domain-providers-documentation"></a>

## SPF, DKIM and DMARC documentation of common providers

- [OVH DNS](https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/)
- [GoDaddy TXT record](https://www.godaddy.com/help/add-a-txt-record-19232)
- [GoDaddy CNAME record](https://www.godaddy.com/help/add-a-cname-record-19236)
- [NameCheap](https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain/)
- [CloudFlare DNS](https://support.cloudflare.com/hc/en-us/articles/360019093151)
- [Squarespace DNS records](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain)
- [Azure DNS](https://docs.microsoft.com/en-us/azure/dns/dns-getstarted-portal)

To fully test the configuration, use the [Mail-Tester](https://www.mail-tester.com/) tool, which
gives a full overview of the content and configuration in one sent email. Mail-Tester can also be
used to configure records for other, lesser-known providers.

#### SEE ALSO
[Using Mail-Tester to set SPF Records for specific carriers](https://www.mail-tester.com/spf/)
