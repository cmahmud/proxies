# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 396
- HTTP: 332 alive / 82 gold
- HTTPS: 193 alive / 20 gold
- SOCKS4: 231 alive / 149 gold
- SOCKS5: 253 alive / 145 gold

## Historical pool

- Discovered: 158238
- Ever alive: 29985
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
