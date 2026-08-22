# SyndProxy private pool

## Current pool

- Alive now: 1041
- Gold now: 403
- HTTP: 353 alive / 89 gold
- HTTPS: 242 alive / 28 gold
- SOCKS4: 222 alive / 149 gold
- SOCKS5: 224 alive / 137 gold

## Historical pool

- Discovered: 165822
- Ever alive: 32338
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
