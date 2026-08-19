# SyndProxy private pool

## Current pool

- Alive now: 1243
- Gold now: 358
- HTTP: 409 alive / 86 gold
- HTTPS: 270 alive / 22 gold
- SOCKS4: 236 alive / 114 gold
- SOCKS5: 328 alive / 136 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22058
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
