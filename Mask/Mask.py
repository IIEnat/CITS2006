import sys
sys.path.append('../SPM')
import SPM


def mask_email(email):
    parts = email.split("@")
    if len(parts) != 2:
        return email
    username, domain = parts
    masked_username = username[0] + "***" + username[-1] if len(username) > 2 else "***"
    return f"{masked_username}@{domain}"

def masked_view_entries():
    entries = SPM.session.query(SPM.PasswordEntry).all()
    print("\n{:<5} {:<15} {:<15} {:<25} {:<20}".format("ID", "Service", "Username", "Email", "Password"))
    print("-" * 80)
    for idx, e in enumerate(entries, start=1):
        masked_email = mask_email(e.email)
        decrypted_password = SPM.decrypt_password(e.password_encrypted)
        print("{:<5} {:<15} {:<15} {:<25} {:<20}".format(idx, e.service, e.username, masked_email, decrypted_password))

# Override the view_entries function with the masked version
SPM.view_entries = masked_view_entries

if __name__ == "__main__":
    SPM.main()
