# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 429
- HTTP: 120 alive / 72 gold
- HTTPS: 74 alive / 26 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45529
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
