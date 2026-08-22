# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 405
- HTTP: 299 alive / 94 gold
- HTTPS: 180 alive / 26 gold
- SOCKS4: 228 alive / 148 gold
- SOCKS5: 214 alive / 137 gold

## Historical pool

- Discovered: 165824
- Ever alive: 32342
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
