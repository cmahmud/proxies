# SyndProxy private pool

## Current pool

- Alive now: 776
- Gold now: 229
- HTTP: 261 alive / 32 gold
- HTTPS: 108 alive / 8 gold
- SOCKS4: 203 alive / 117 gold
- SOCKS5: 204 alive / 72 gold

## Historical pool

- Discovered: 93710
- Ever alive: 9324
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
