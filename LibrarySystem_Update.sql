UPDATE Admins SET First_Name = ?, Last_Name = ?, Email = ?, Access_Level = ? WHERE Admin_ID = ?;
UPDATE Authors SET First_Name = ?, Last_Name = ?, Biography = ? WHERE Author_ID = ?;
UPDATE Books SET Title = ?, Author_ID = ?, Genre_ID = ?, ISBN = ?, Publication_Year = ? WHERE Book_ID = ?;
UPDATE Checkouts SET Member_ID = ?, Copy_ID = ?, Checkout_Date = ?, Due_Date = ?, Return_Date = ?, Librarian_ID = ? WHERE Checkout_ID = ?;
UPDATE Copy SET Book_ID = ?, Availability_Status = ? WHERE Copy_ID = ?;
UPDATE Fines SET Member_ID = ?, Checkout_ID = ?, Amount = ?, Payment_Status = ? WHERE Fine_ID = ?;
UPDATE Genre SET Genre_Name = ? WHERE Genre_ID = ?;
UPDATE Librarians SET First_Name = ?, Last_Name = ?, Email = ? WHERE Librarian_ID = ?;
UPDATE Members SET First_Name = ?, Last_Name = ?, Email = ?, Subscription_ID = ? WHERE Member_ID = ?;
UPDATE Reservations SET Member_ID = ?, Copy_ID = ?, Reservation_Date = ?, CheckoutsCheckout_ID = ? WHERE Reservation_ID = ?;
UPDATE Reviews SET Member_ID = ?, Book_ID = ?, Review_Text = ?, Ratings = ? WHERE Review_ID = ?;
UPDATE Subscriptions SET Subscription_Type = ?, Fee = ?, Duration = ? WHERE Subscription_ID = ?;