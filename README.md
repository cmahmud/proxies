# SyndProxy private pool

## Current pool

- Alive now: 953
- Gold now: 468
- HTTP: 315 alive / 135 gold
- HTTPS: 239 alive / 90 gold
- SOCKS4: 203 alive / 129 gold
- SOCKS5: 196 alive / 114 gold

## Historical pool

- Discovered: 117111
- Ever alive: 17361
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
