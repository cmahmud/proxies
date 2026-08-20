# SyndProxy private pool

## Current pool

- Alive now: 1492
- Gold now: 425
- HTTP: 562 alive / 120 gold
- HTTPS: 354 alive / 22 gold
- SOCKS4: 246 alive / 129 gold
- SOCKS5: 330 alive / 154 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22681
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
