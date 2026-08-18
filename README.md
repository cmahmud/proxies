# SyndProxy private pool

## Current pool

- Alive now: 922
- Gold now: 214
- HTTP: 484 alive / 36 gold
- HTTPS: 138 alive / 10 gold
- SOCKS4: 137 alive / 97 gold
- SOCKS5: 163 alive / 71 gold

## Historical pool

- Discovered: 82966
- Ever alive: 5479
- Ever gold: 287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
