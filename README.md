# SyndProxy private pool

## Current pool

- Alive now: 734
- Gold now: 267
- HTTP: 197 alive / 33 gold
- HTTPS: 143 alive / 4 gold
- SOCKS4: 206 alive / 132 gold
- SOCKS5: 188 alive / 98 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10666
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
