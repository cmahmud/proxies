# SyndProxy private pool

## Current pool

- Alive now: 636
- Gold now: 223
- HTTP: 180 alive / 30 gold
- HTTPS: 78 alive / 8 gold
- SOCKS4: 191 alive / 106 gold
- SOCKS5: 187 alive / 79 gold

## Historical pool

- Discovered: 86707
- Ever alive: 6452
- Ever gold: 300

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
