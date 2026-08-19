# SyndProxy private pool

## Current pool

- Alive now: 1352
- Gold now: 414
- HTTP: 494 alive / 82 gold
- HTTPS: 318 alive / 17 gold
- SOCKS4: 243 alive / 157 gold
- SOCKS5: 297 alive / 158 gold

## Historical pool

- Discovered: 134523
- Ever alive: 21899
- Ever gold: 888

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
