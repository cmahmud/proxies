# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 448
- HTTP: 121 alive / 89 gold
- HTTPS: 66 alive / 36 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 204 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44261
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
