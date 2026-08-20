# SyndProxy private pool

## Current pool

- Alive now: 708
- Gold now: 354
- HTTP: 185 alive / 73 gold
- HTTPS: 132 alive / 19 gold
- SOCKS4: 214 alive / 145 gold
- SOCKS5: 177 alive / 117 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25350
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
