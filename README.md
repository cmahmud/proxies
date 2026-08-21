# SyndProxy private pool

## Current pool

- Alive now: 801
- Gold now: 382
- HTTP: 236 alive / 79 gold
- HTTPS: 130 alive / 19 gold
- SOCKS4: 219 alive / 136 gold
- SOCKS5: 216 alive / 148 gold

## Historical pool

- Discovered: 157559
- Ever alive: 29766
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
