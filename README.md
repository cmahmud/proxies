# SyndProxy private pool

## Current pool

- Alive now: 1022
- Gold now: 353
- HTTP: 353 alive / 71 gold
- HTTPS: 218 alive / 17 gold
- SOCKS4: 202 alive / 122 gold
- SOCKS5: 249 alive / 143 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15773
- Ever gold: 504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
