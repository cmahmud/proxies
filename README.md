# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 425
- HTTP: 345 alive / 112 gold
- HTTPS: 211 alive / 33 gold
- SOCKS4: 217 alive / 136 gold
- SOCKS5: 247 alive / 144 gold

## Historical pool

- Discovered: 160275
- Ever alive: 30743
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
