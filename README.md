# SyndProxy private pool

## Current pool

- Alive now: 1167
- Gold now: 248
- HTTP: 395 alive / 27 gold
- HTTPS: 288 alive / 10 gold
- SOCKS4: 236 alive / 109 gold
- SOCKS5: 248 alive / 102 gold

## Historical pool

- Discovered: 94370
- Ever alive: 10174
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
