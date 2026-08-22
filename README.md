# SyndProxy private pool

## Current pool

- Alive now: 858
- Gold now: 404
- HTTP: 262 alive / 89 gold
- HTTPS: 148 alive / 28 gold
- SOCKS4: 194 alive / 125 gold
- SOCKS5: 254 alive / 162 gold

## Historical pool

- Discovered: 164921
- Ever alive: 32156
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
