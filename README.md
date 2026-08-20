# SyndProxy private pool

## Current pool

- Alive now: 684
- Gold now: 381
- HTTP: 174 alive / 69 gold
- HTTPS: 105 alive / 19 gold
- SOCKS4: 199 alive / 139 gold
- SOCKS5: 206 alive / 154 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25571
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
