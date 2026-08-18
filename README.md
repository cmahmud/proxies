# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 257
- HTTP: 384 alive / 32 gold
- HTTPS: 173 alive / 4 gold
- SOCKS4: 214 alive / 117 gold
- SOCKS5: 220 alive / 104 gold

## Historical pool

- Discovered: 99106
- Ever alive: 11774
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
