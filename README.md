# SyndProxy private pool

## Current pool

- Alive now: 1119
- Gold now: 258
- HTTP: 435 alive / 32 gold
- HTTPS: 214 alive / 4 gold
- SOCKS4: 231 alive / 116 gold
- SOCKS5: 239 alive / 106 gold

## Historical pool

- Discovered: 95405
- Ever alive: 10999
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
