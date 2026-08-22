# SyndProxy private pool

## Current pool

- Alive now: 762
- Gold now: 414
- HTTP: 199 alive / 89 gold
- HTTPS: 139 alive / 26 gold
- SOCKS4: 199 alive / 140 gold
- SOCKS5: 225 alive / 159 gold

## Historical pool

- Discovered: 163857
- Ever alive: 31961
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
