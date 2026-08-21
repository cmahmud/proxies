# SyndProxy private pool

## Current pool

- Alive now: 934
- Gold now: 391
- HTTP: 286 alive / 93 gold
- HTTPS: 218 alive / 23 gold
- SOCKS4: 194 alive / 135 gold
- SOCKS5: 236 alive / 140 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27888
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
