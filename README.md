# IP-Classifier-Firewall-Simulator
A Python-based project for IPv4 address classification and Packet Filtering Firewall simulation.
ეს პროექტი შემუშავებულია Python-ის გამოყენებით.
ის ახორციელებს IPv4 მისამართების კლასიფიკაციას და ახდენს Packet Filtering Firewall-ის ძირითადი ოპერაციის სიმულირებას.
ამ პროექტის მიზანია IPv4 კლასიფიკაციის და ქსელის უსაფრთხოების ძირითადი კონცეფციების გაგება Python-ის პროგრამირების საშუალებით.
პროექტის მახასიათებლები: - IPv4 address validation
- IP address class identification (A, B, C, D, E)
- Private and Public IP identification
- Port validation
- TCP and UDP protocol selection
- Firewall rule checking
- ALLOW / BLOCK decisions
  
გამოყენებული ტექნოლოგიები: Python 3
- ipaddress module
- Visual Studio Code
  
Firewall-ის წესები:

| Protocol | Port | Action |
|----------|------|--------|
| TCP | 22 | BLOCK |
| TCP | 80 | ALLOW |
| TCP | 443 | ALLOW |
| UDP | 53 | ALLOW |

Default Policy: BLOCK
