# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 304
- HTTP: 372 alive / 31 gold
- HTTPS: 207 alive / 4 gold
- SOCKS4: 219 alive / 142 gold
- SOCKS5: 212 alive / 127 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13439
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
