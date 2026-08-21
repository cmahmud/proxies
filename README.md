# SyndProxy private pool

## Current pool

- Alive now: 1017
- Gold now: 417
- HTTP: 335 alive / 91 gold
- HTTPS: 224 alive / 21 gold
- SOCKS4: 212 alive / 147 gold
- SOCKS5: 246 alive / 158 gold

## Historical pool

- Discovered: 156426
- Ever alive: 29513
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
