# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 426
- HTTP: 324 alive / 107 gold
- HTTPS: 200 alive / 33 gold
- SOCKS4: 219 alive / 138 gold
- SOCKS5: 243 alive / 148 gold

## Historical pool

- Discovered: 160258
- Ever alive: 30710
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
