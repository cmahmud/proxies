# SyndProxy validated proxy pool

## Current pool

- Alive now: 358
- Gold now: 297
- HTTP: 66 alive / 58 gold
- HTTPS: 70 alive / 20 gold
- SOCKS4: 73 alive / 73 gold
- SOCKS5: 149 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47681
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
