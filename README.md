# SyndProxy private pool

## Current pool

- Alive now: 1104
- Gold now: 510
- HTTP: 387 alive / 148 gold
- HTTPS: 290 alive / 91 gold
- SOCKS4: 218 alive / 142 gold
- SOCKS5: 209 alive / 129 gold

## Historical pool

- Discovered: 117170
- Ever alive: 17699
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
