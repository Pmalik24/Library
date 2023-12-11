use library;

-- DELIMITER //
-- CREATE FUNCTION GetAverageBookRating(bookId INT) RETURNS DECIMAL(3, 2) DETERMINISTIC
-- BEGIN
--     DECLARE avgRating DECIMAL(3, 2);
--     SELECT AVG(R.Ratings) INTO avgRating
--     FROM Reviews R
--     WHERE R.Book_ID = bookId;
--     RETURN COALESCE(avgRating, 0);
-- END //
-- DELIMITER ;



-- DELIMITER //
-- CREATE FUNCTION IsBookAvailable(bookId INT) RETURNS BOOLEAN DETERMINISTIC
-- BEGIN DECLARE availability BOOLEAN;
--     SELECT CASE WHEN COUNT(*) > 0 THEN TRUE ELSE FALSE END INTO availability
--     FROM Copy
--     WHERE Book_ID = bookId AND Availability_Status = 'Available';
--     RETURN availability;
-- END //
-- DELIMITER ;


-- DELIMITER //
-- CREATE FUNCTION GetMemberSubscriptionFee(memberId INT) RETURNS DECIMAL(10, 2) DETERMINISTIC
-- BEGIN DECLARE subscriptionFee DECIMAL(10, 2);
-- 	SELECT S.Fee INTO subscriptionFee FROM Members M
--     JOIN Subscriptions S ON M.Subscription_ID = S.Subscription_ID
--     WHERE M.Member_ID = memberId;
--     RETURN COALESCE(subscriptionFee, 0);
-- END //
-- DELIMITER ;

-- DELIMITER //
-- CREATE TRIGGER UpdateMemberTotalFine 
-- AFTER INSERT ON Fines
-- FOR EACH ROW 
-- BEGIN
--     DECLARE totalFine DECIMAL(10, 2);
--     SELECT COALESCE(SUM(Amount), 0) INTO totalFine
--     FROM Fines
--     WHERE Member_ID = NEW.Member_ID;
--     UPDATE Members
--     SET Total_Fine = totalFine
--     WHERE Member_ID = NEW.Member_ID;
-- END //
-- DELIMITER ;

