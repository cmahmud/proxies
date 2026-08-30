# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 429
- HTTP: 120 alive / 81 gold
- HTTPS: 60 alive / 22 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44309
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
