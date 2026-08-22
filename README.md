# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 400
- HTTP: 328 alive / 89 gold
- HTTPS: 237 alive / 25 gold
- SOCKS4: 222 alive / 137 gold
- SOCKS5: 244 alive / 149 gold

## Historical pool

- Discovered: 164248
- Ever alive: 32106
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
