# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 425
- HTTP: 119 alive / 81 gold
- HTTPS: 59 alive / 19 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 199 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44329
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
