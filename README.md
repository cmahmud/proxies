# SyndProxy private pool

## Current pool

- Alive now: 1239
- Gold now: 543
- HTTP: 442 alive / 169 gold
- HTTPS: 362 alive / 78 gold
- SOCKS4: 228 alive / 148 gold
- SOCKS5: 207 alive / 148 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19758
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
