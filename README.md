# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 448
- HTTP: 140 alive / 88 gold
- HTTPS: 79 alive / 34 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 215 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44221
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
