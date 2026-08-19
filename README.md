# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 543
- HTTP: 375 alive / 162 gold
- HTTPS: 238 alive / 91 gold
- SOCKS4: 217 alive / 145 gold
- SOCKS5: 203 alive / 145 gold

## Historical pool

- Discovered: 123921
- Ever alive: 19153
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
