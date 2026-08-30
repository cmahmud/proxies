# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 425
- HTTP: 115 alive / 80 gold
- HTTPS: 60 alive / 20 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 202 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44332
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
