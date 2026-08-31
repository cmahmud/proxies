# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 485
- HTTP: 145 alive / 100 gold
- HTTPS: 138 alive / 46 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 199 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44995
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
