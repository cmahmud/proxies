# SyndProxy private pool

## Current pool

- Alive now: 960
- Gold now: 409
- HTTP: 282 alive / 94 gold
- HTTPS: 215 alive / 19 gold
- SOCKS4: 218 alive / 150 gold
- SOCKS5: 245 alive / 146 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29260
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
