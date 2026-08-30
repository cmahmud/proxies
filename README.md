# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 429
- HTTP: 116 alive / 81 gold
- HTTPS: 63 alive / 22 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 196 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44312
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
