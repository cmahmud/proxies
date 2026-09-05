# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 279
- HTTP: 129 alive / 61 gold
- HTTPS: 44 alive / 20 gold
- SOCKS4: 152 alive / 65 gold
- SOCKS5: 240 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47782
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
