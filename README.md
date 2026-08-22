# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 404
- HTTP: 316 alive / 75 gold
- HTTPS: 229 alive / 22 gold
- SOCKS4: 228 alive / 150 gold
- SOCKS5: 256 alive / 157 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32295
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
