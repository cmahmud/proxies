# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 476
- HTTP: 129 alive / 97 gold
- HTTPS: 111 alive / 41 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 200 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44923
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
