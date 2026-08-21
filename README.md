# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 361
- HTTP: 329 alive / 81 gold
- HTTPS: 248 alive / 19 gold
- SOCKS4: 191 alive / 126 gold
- SOCKS5: 238 alive / 135 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29844
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
