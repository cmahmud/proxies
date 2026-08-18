# SyndProxy private pool

## Current pool

- Alive now: 973
- Gold now: 287
- HTTP: 340 alive / 27 gold
- HTTPS: 209 alive / 3 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 207 alive / 117 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13445
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
