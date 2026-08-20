# SyndProxy private pool

## Current pool

- Alive now: 720
- Gold now: 357
- HTTP: 195 alive / 75 gold
- HTTPS: 129 alive / 22 gold
- SOCKS4: 219 alive / 143 gold
- SOCKS5: 177 alive / 117 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25349
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
