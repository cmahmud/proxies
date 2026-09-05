# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 282
- HTTP: 66 alive / 55 gold
- HTTPS: 61 alive / 20 gold
- SOCKS4: 143 alive / 69 gold
- SOCKS5: 246 alive / 138 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47750
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
