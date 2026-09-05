# SyndProxy validated proxy pool

## Current pool

- Alive now: 323
- Gold now: 265
- HTTP: 67 alive / 53 gold
- HTTPS: 32 alive / 9 gold
- SOCKS4: 75 alive / 67 gold
- SOCKS5: 149 alive / 136 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47681
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
