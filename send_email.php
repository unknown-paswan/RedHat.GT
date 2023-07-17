<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST['name'];
  $email = $_POST['email'];
  $subject = $_POST['subject'];
  $message = $_POST['message'];
  
  // Set the recipient email address
  $to = "unknown.paswan.g.t.m@gmail.com";
  
  // Set the email subject and body
  $email_subject = "New Contact Form Submission: $subject";
  $email_body = "You have received a new message from your website contact form:\n\n";
  $email_body .= "Name: $name\n";
  $email_body .= "Email: $email\n";
  $email_body .= "Message:\n$message";
  
  // Set the email headers
  $headers = "From: $name <$email>\r\n";
  $headers .= "Reply-To: $email\r\n";
  
  // Send the email
  if (mail($to, $email_subject, $email_body, $headers)) {
    echo "Message sent successfully!";
  } else {
    echo "Error sending message. Please try again.";
  }
}
?>
