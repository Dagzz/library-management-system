from src.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repository):
        self.user_repository = repository
        # self.loan_repository = LoanRepository()

    def create_user(self, first_name, last_name, login, mail, date_of_birth, phone, address):
        """
        Creates a new user (with default is_active=True, etc.).
        Enforces unique login or mail if needed.
        """
        existing_user = self.user_repository.find_by_login(login)
        if existing_user:
            raise ValueError("Login is already used by another user.")

        new_user = self.user_repository.create(
            first_name=first_name,
            last_name=last_name,
            login=login,
            mail=mail,
            date_of_birth=date_of_birth,
            phone=phone,
            address=address,
        )
        return new_user

    def update_user_info(self, user_id, **kwargs):
        """
        Updates user info (e.g., phone, address).
        """
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        updated_user = self.user_repository.update(user, **kwargs)
        return updated_user

    def block_user(self, user_id):
        """
        Block a user if too many late returns or as decided by an admin.
        """
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        # Additional logic if needed, e.g., checking user’s late returns
        user.is_active = False
        return self.user_repository.update(user)

    def get_user_by_id(self, user_id):
        return self.user_repository.find_by_id(user_id)

    def delete_user(self, user_id):
        """
        Deletes a user (e.g., if an admin decides).
        Possibly check if user still has outstanding loans.
        """
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        # Check for outstanding loans or reservations before deleting
        self.user_repository.delete(user)
        return True
