# SyndProxy validated proxy pool

## Current pool

- Alive now: 380
- Gold now: 281
- HTTP: 67 alive / 54 gold
- HTTPS: 89 alive / 15 gold
- SOCKS4: 75 alive / 70 gold
- SOCKS5: 149 alive / 142 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47681
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
