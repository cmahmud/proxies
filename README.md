# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 387
- HTTP: 114 alive / 55 gold
- HTTPS: 42 alive / 12 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 194 alive / 161 gold

## Historical pool

- Discovered: 178284
- Ever alive: 33363
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
