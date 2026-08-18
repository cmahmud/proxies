# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 257
- HTTP: 300 alive / 28 gold
- HTTPS: 192 alive / 5 gold
- SOCKS4: 207 alive / 115 gold
- SOCKS5: 226 alive / 109 gold

## Historical pool

- Discovered: 99106
- Ever alive: 11821
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
