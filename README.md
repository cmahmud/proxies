# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 391
- HTTP: 108 alive / 64 gold
- HTTPS: 58 alive / 14 gold
- SOCKS4: 170 alive / 153 gold
- SOCKS5: 188 alive / 160 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33169
- Ever gold: 1229

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
