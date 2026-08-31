# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 423
- HTTP: 89 alive / 62 gold
- HTTPS: 71 alive / 29 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45490
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
