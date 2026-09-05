# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 303
- HTTP: 161 alive / 76 gold
- HTTPS: 39 alive / 23 gold
- SOCKS4: 225 alive / 68 gold
- SOCKS5: 199 alive / 136 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47803
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
