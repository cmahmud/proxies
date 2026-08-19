# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 467
- HTTP: 370 alive / 120 gold
- HTTPS: 282 alive / 85 gold
- SOCKS4: 215 alive / 142 gold
- SOCKS5: 185 alive / 120 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17467
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
