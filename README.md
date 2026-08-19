# SyndProxy private pool

## Current pool

- Alive now: 1177
- Gold now: 405
- HTTP: 360 alive / 94 gold
- HTTPS: 251 alive / 15 gold
- SOCKS4: 253 alive / 148 gold
- SOCKS5: 313 alive / 148 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21096
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
