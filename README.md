# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 420
- HTTP: 305 alive / 88 gold
- HTTPS: 213 alive / 22 gold
- SOCKS4: 234 alive / 141 gold
- SOCKS5: 286 alive / 169 gold

## Historical pool

- Discovered: 164956
- Ever alive: 32223
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
