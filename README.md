# SyndProxy private pool

## Current pool

- Alive now: 1299
- Gold now: 428
- HTTP: 483 alive / 106 gold
- HTTPS: 297 alive / 26 gold
- SOCKS4: 207 alive / 141 gold
- SOCKS5: 312 alive / 155 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22646
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
