# Workflow Diagram

```text
START -> Main Menu
          |
          +-> Create Account -> Save -> Main Menu
          |
          +-> Login -> Check PIN
                       |
                       +-> Invalid -> Main Menu
                       |
                       +-> Valid -> User Menu
                                      |
                       +--------------+--------------+
                       |              |              |
                    Deposit        Withdraw       Transfer
                       |              |              |
                       +--------------+--------------+
                                      |
                              Save Transaction
                                      |
                         History / Summary / PIN
                                      |
                                   Logout
                                      |
                                  Main Menu
                                      |
                                     END
```
