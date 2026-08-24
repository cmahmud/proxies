# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 382
- HTTP: 106 alive / 56 gold
- HTTPS: 51 alive / 12 gold
- SOCKS4: 168 alive / 155 gold
- SOCKS5: 183 alive / 159 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33457
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
