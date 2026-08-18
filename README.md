# SyndProxy private pool

## Current pool

- Alive now: 762
- Gold now: 229
- HTTP: 232 alive / 32 gold
- HTTPS: 115 alive / 8 gold
- SOCKS4: 211 alive / 117 gold
- SOCKS5: 204 alive / 72 gold

## Historical pool

- Discovered: 93710
- Ever alive: 9325
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
