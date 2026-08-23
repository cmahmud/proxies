# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 339
- HTTP: 93 alive / 30 gold
- HTTPS: 59 alive / 8 gold
- SOCKS4: 184 alive / 148 gold
- SOCKS5: 207 alive / 153 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32956
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
