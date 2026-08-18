# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 256
- HTTP: 424 alive / 30 gold
- HTTPS: 179 alive / 4 gold
- SOCKS4: 210 alive / 117 gold
- SOCKS5: 221 alive / 105 gold

## Historical pool

- Discovered: 99106
- Ever alive: 11776
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
