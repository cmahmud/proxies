# SyndProxy private pool

## Current pool

- Alive now: 1067
- Gold now: 404
- HTTP: 359 alive / 85 gold
- HTTPS: 215 alive / 26 gold
- SOCKS4: 240 alive / 149 gold
- SOCKS5: 253 alive / 144 gold

## Historical pool

- Discovered: 165502
- Ever alive: 32282
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
