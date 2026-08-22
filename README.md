# SyndProxy private pool

## Current pool

- Alive now: 1052
- Gold now: 443
- HTTP: 326 alive / 95 gold
- HTTPS: 212 alive / 28 gold
- SOCKS4: 235 alive / 149 gold
- SOCKS5: 279 alive / 171 gold

## Historical pool

- Discovered: 161013
- Ever alive: 31026
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
