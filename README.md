# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 380
- HTTP: 328 alive / 89 gold
- HTTPS: 262 alive / 26 gold
- SOCKS4: 159 alive / 103 gold
- SOCKS5: 257 alive / 162 gold

## Historical pool

- Discovered: 166625
- Ever alive: 32458
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
