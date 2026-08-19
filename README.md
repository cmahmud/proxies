# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 419
- HTTP: 391 alive / 90 gold
- HTTPS: 288 alive / 23 gold
- SOCKS4: 243 alive / 140 gold
- SOCKS5: 294 alive / 166 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22270
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
