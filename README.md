# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 403
- HTTP: 218 alive / 79 gold
- HTTPS: 237 alive / 20 gold
- SOCKS4: 209 alive / 145 gold
- SOCKS5: 228 alive / 159 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26513
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
