# SyndProxy private pool

## Current pool

- Alive now: 1241
- Gold now: 418
- HTTP: 408 alive / 90 gold
- HTTPS: 282 alive / 22 gold
- SOCKS4: 245 alive / 140 gold
- SOCKS5: 306 alive / 166 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22246
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
