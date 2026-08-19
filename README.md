# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 475
- HTTP: 382 alive / 122 gold
- HTTPS: 232 alive / 71 gold
- SOCKS4: 219 alive / 143 gold
- SOCKS5: 247 alive / 139 gold

## Historical pool

- Discovered: 113577
- Ever alive: 16889
- Ever gold: 626

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
