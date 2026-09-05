# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 295
- HTTP: 189 alive / 71 gold
- HTTPS: 43 alive / 21 gold
- SOCKS4: 219 alive / 68 gold
- SOCKS5: 214 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47801
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
