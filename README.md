# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 405
- HTTP: 308 alive / 93 gold
- HTTPS: 216 alive / 15 gold
- SOCKS4: 251 alive / 147 gold
- SOCKS5: 285 alive / 150 gold

## Historical pool

- Discovered: 131828
- Ever alive: 21082
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
