# SyndProxy private pool

## Current pool

- Alive now: 807
- Gold now: 383
- HTTP: 183 alive / 75 gold
- HTTPS: 183 alive / 19 gold
- SOCKS4: 220 alive / 150 gold
- SOCKS5: 221 alive / 139 gold

## Historical pool

- Discovered: 149510
- Ever alive: 26890
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
