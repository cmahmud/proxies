# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 451
- HTTP: 145 alive / 89 gold
- HTTPS: 76 alive / 36 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 213 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44220
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
