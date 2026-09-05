# SyndProxy validated proxy pool

## Current pool

- Alive now: 399
- Gold now: 316
- HTTP: 102 alive / 80 gold
- HTTPS: 55 alive / 24 gold
- SOCKS4: 84 alive / 74 gold
- SOCKS5: 158 alive / 138 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47934
- Ever gold: 1505

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
