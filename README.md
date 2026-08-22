# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 408
- HTTP: 284 alive / 81 gold
- HTTPS: 210 alive / 25 gold
- SOCKS4: 195 alive / 134 gold
- SOCKS5: 261 alive / 168 gold

## Historical pool

- Discovered: 161927
- Ever alive: 31194
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
