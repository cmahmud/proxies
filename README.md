# SyndProxy private pool

## Current pool

- Alive now: 608
- Gold now: 210
- HTTP: 140 alive / 21 gold
- HTTPS: 82 alive / 8 gold
- SOCKS4: 179 alive / 99 gold
- SOCKS5: 207 alive / 82 gold

## Historical pool

- Discovered: 91002
- Ever alive: 8004
- Ever gold: 346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
