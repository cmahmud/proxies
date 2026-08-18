# SyndProxy private pool

## Current pool

- Alive now: 922
- Gold now: 296
- HTTP: 306 alive / 35 gold
- HTTPS: 183 alive / 5 gold
- SOCKS4: 220 alive / 130 gold
- SOCKS5: 213 alive / 126 gold

## Historical pool

- Discovered: 102848
- Ever alive: 13233
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
