# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 388
- HTTP: 308 alive / 75 gold
- HTTPS: 214 alive / 24 gold
- SOCKS4: 229 alive / 142 gold
- SOCKS5: 238 alive / 147 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29578
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
