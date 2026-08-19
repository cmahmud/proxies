# SyndProxy private pool

## Current pool

- Alive now: 1171
- Gold now: 403
- HTTP: 374 alive / 76 gold
- HTTPS: 279 alive / 13 gold
- SOCKS4: 255 alive / 152 gold
- SOCKS5: 263 alive / 162 gold

## Historical pool

- Discovered: 131115
- Ever alive: 20624
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
