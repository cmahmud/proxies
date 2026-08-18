# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 288
- HTTP: 309 alive / 26 gold
- HTTPS: 169 alive / 4 gold
- SOCKS4: 207 alive / 140 gold
- SOCKS5: 212 alive / 118 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13475
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
