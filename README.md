# SyndProxy private pool

## Current pool

- Alive now: 1190
- Gold now: 416
- HTTP: 388 alive / 90 gold
- HTTPS: 274 alive / 23 gold
- SOCKS4: 245 alive / 140 gold
- SOCKS5: 283 alive / 163 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22289
- Ever gold: 895

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
