# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 430
- HTTP: 97 alive / 74 gold
- HTTPS: 60 alive / 28 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44436
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
