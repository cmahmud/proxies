# SyndProxy private pool

## Current pool

- Alive now: 976
- Gold now: 475
- HTTP: 307 alive / 121 gold
- HTTPS: 207 alive / 70 gold
- SOCKS4: 226 alive / 136 gold
- SOCKS5: 236 alive / 148 gold

## Historical pool

- Discovered: 113575
- Ever alive: 16847
- Ever gold: 625

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
