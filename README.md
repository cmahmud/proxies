# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 430
- HTTP: 101 alive / 78 gold
- HTTPS: 56 alive / 25 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44433
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
