# SyndProxy validated proxy pool

## Current pool

- Alive now: 677
- Gold now: 477
- HTTP: 165 alive / 100 gold
- HTTPS: 114 alive / 39 gold
- SOCKS4: 179 alive / 163 gold
- SOCKS5: 219 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45254
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
