# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 429
- HTTP: 117 alive / 74 gold
- HTTPS: 69 alive / 26 gold
- SOCKS4: 167 alive / 162 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44375
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
