# SyndProxy private pool

## Current pool

- Alive now: 1229
- Gold now: 408
- HTTP: 402 alive / 95 gold
- HTTPS: 269 alive / 15 gold
- SOCKS4: 248 alive / 150 gold
- SOCKS5: 310 alive / 148 gold

## Historical pool

- Discovered: 131837
- Ever alive: 21139
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
