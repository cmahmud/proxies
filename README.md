# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 341
- HTTP: 300 alive / 55 gold
- HTTPS: 187 alive / 13 gold
- SOCKS4: 237 alive / 139 gold
- SOCKS5: 217 alive / 134 gold

## Historical pool

- Discovered: 107138
- Ever alive: 15013
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
