# SyndProxy private pool

## Current pool

- Alive now: 591
- Gold now: 214
- HTTP: 141 alive / 21 gold
- HTTPS: 78 alive / 9 gold
- SOCKS4: 163 alive / 98 gold
- SOCKS5: 209 alive / 86 gold

## Historical pool

- Discovered: 91520
- Ever alive: 8004
- Ever gold: 346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
