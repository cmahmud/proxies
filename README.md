# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 391
- HTTP: 98 alive / 74 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 166 alive / 149 gold
- SOCKS5: 173 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48204
- Ever gold: 1523

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
