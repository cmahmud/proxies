# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 447
- HTTP: 140 alive / 89 gold
- HTTPS: 85 alive / 34 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 207 alive / 164 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44206
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
