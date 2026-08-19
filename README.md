# SyndProxy private pool

## Current pool

- Alive now: 1208
- Gold now: 416
- HTTP: 387 alive / 89 gold
- HTTPS: 284 alive / 24 gold
- SOCKS4: 249 alive / 140 gold
- SOCKS5: 288 alive / 163 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22286
- Ever gold: 895

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
