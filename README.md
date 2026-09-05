# SyndProxy validated proxy pool

## Current pool

- Alive now: 681
- Gold now: 296
- HTTP: 277 alive / 76 gold
- HTTPS: 37 alive / 21 gold
- SOCKS4: 183 alive / 65 gold
- SOCKS5: 184 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47819
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
