# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 423
- HTTP: 92 alive / 67 gold
- HTTPS: 70 alive / 26 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45476
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
