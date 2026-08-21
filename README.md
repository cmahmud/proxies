# SyndProxy private pool

## Current pool

- Alive now: 1115
- Gold now: 446
- HTTP: 363 alive / 94 gold
- HTTPS: 262 alive / 33 gold
- SOCKS4: 231 alive / 163 gold
- SOCKS5: 259 alive / 156 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30257
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
