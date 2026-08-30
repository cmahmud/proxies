# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 429
- HTTP: 114 alive / 80 gold
- HTTPS: 61 alive / 21 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44313
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
