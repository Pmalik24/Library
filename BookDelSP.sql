use library;
-- ==================================================================================================
-- Procedure: DeleteBookCopy
-- ==================================================================================================
-- Description: 
--    Deletes a copy of a book from the library's database. The procedure first checks if the book
--    exists and if it has any associated unpaid fines. It also checks whether the book is currently
--    checked out or reserved. If these conditions are met, the procedure proceeds to delete a copy
--    of the book. If it's the last copy, it also removes related records from the Books_Authors, 
--    Reviews, and Books tables.
--
-- Parameters:
--    xbook_id INT - The ID of the book for which a copy needs to be deleted.
--
-- Usage:
--    CALL DeleteBookCopy(123); -- where 123 is the book ID
--
-- Process:
--    1. Checks if the book exists in the Copy table.
--    2. Checks for any unpaid fines associated with the book.
--    3. Verifies if the book is not currently checked out or reserved.
--    4. Deletes a copy of the book if the above conditions are met.
--    5. If it's the last copy, removes the book from Books_Authors, Reviews, and Books tables.
--    6. Returns a message indicating the outcome of the operation.
--
-- Note:
--    - The procedure handles integrity constraints to maintain database consistency.
--    - It is designed to ensure that books with outstanding obligations are not removed.
--
-- ==================================================================================================
DELIMITER //

CREATE PROCEDURE DeleteBookCopy(IN xbook_id INT)
BEGIN
    PROC_BLOCK: BEGIN
        DECLARE total_copies INT DEFAULT 0;
        DECLARE copy_id_to_delete INT;

        -- Check if the book exists
        SELECT COUNT(*) INTO total_copies FROM Copy WHERE Book_ID = xbook_id;
        IF total_copies = 0 THEN
            SELECT 'Book does not exist.' AS message;
            LEAVE PROC_BLOCK;
        END IF;

        -- Check for unpaid fines associated with the book
        IF EXISTS (
            SELECT 1 FROM Fines 
            JOIN Checkouts ON Fines.Checkout_ID = Checkouts.Checkout_ID 
            WHERE Checkouts.Copy_ID IN (SELECT Copy_ID FROM Copy WHERE Book_ID = xbook_id) 
            AND Fines.Payment_Status = 'Unpaid'
        ) THEN
            SELECT 'Cannot delete book as it has associated unpaid fines.' AS message;
            LEAVE PROC_BLOCK;
        END IF;

        -- Check for active reservations or checkouts
        IF EXISTS (
            SELECT 1 FROM Copy 
            WHERE Book_ID = xbook_id AND Availability_Status = 'Available'
            AND NOT EXISTS (
               SELECT 1 FROM Reservations WHERE Copy_ID = Copy.Copy_ID
            )
            AND NOT EXISTS (
                 SELECT 1 FROM Checkouts WHERE Copy_ID = Copy.Copy_ID AND Return_Date IS NULL
             )
        ) THEN
            SELECT Copy_ID INTO copy_id_to_delete FROM Copy WHERE Book_ID = xbook_id LIMIT 1;

            DELETE FROM Copy WHERE Copy_ID = copy_id_to_delete;

            IF total_copies = 1 THEN
                DELETE FROM Books_Authors WHERE BooksBook_ID = xbook_id;
                DELETE FROM Reviews WHERE Book_ID = xbook_id;
                DELETE FROM Books WHERE Book_ID = xbook_id;
                SELECT 'Last copy deleted. Book removed from library.' AS message;
            ELSE
                SELECT 'Copy deleted. More copies available.' AS message;
            END IF;
        ELSE
            SELECT 'Cannot delete book as it is currently checked out or reserved.' AS message;
        END IF;
    END PROC_BLOCK;
END //

DELIMITER ;