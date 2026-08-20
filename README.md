# SyndProxy private pool

## Current pool

- Alive now: 1429
- Gold now: 454
- HTTP: 519 alive / 130 gold
- HTTPS: 339 alive / 35 gold
- SOCKS4: 238 alive / 134 gold
- SOCKS5: 333 alive / 155 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22687
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
