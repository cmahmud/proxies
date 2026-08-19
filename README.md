# SyndProxy private pool

## Current pool

- Alive now: 1249
- Gold now: 357
- HTTP: 419 alive / 87 gold
- HTTPS: 271 alive / 20 gold
- SOCKS4: 236 alive / 114 gold
- SOCKS5: 323 alive / 136 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22069
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
