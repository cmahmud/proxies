# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 444
- HTTP: 144 alive / 89 gold
- HTTPS: 77 alive / 32 gold
- SOCKS4: 162 alive / 158 gold
- SOCKS5: 197 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44283
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
