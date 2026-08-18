# SyndProxy private pool

## Current pool

- Alive now: 958
- Gold now: 288
- HTTP: 333 alive / 27 gold
- HTTPS: 198 alive / 4 gold
- SOCKS4: 217 alive / 140 gold
- SOCKS5: 210 alive / 117 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13445
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
