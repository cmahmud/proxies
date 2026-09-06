# SyndProxy validated proxy pool

## Current pool

- Alive now: 485
- Gold now: 395
- HTTP: 102 alive / 76 gold
- HTTPS: 46 alive / 17 gold
- SOCKS4: 166 alive / 150 gold
- SOCKS5: 171 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48203
- Ever gold: 1523

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
