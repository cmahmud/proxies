# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 391
- HTTP: 389 alive / 88 gold
- HTTPS: 300 alive / 14 gold
- SOCKS4: 214 alive / 128 gold
- SOCKS5: 253 alive / 161 gold

## Historical pool

- Discovered: 131853
- Ever alive: 21277
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
