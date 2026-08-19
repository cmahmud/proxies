# SyndProxy private pool

## Current pool

- Alive now: 1205
- Gold now: 363
- HTTP: 407 alive / 89 gold
- HTTPS: 255 alive / 21 gold
- SOCKS4: 236 alive / 117 gold
- SOCKS5: 307 alive / 136 gold

## Historical pool

- Discovered: 134552
- Ever alive: 22075
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
