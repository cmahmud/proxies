# SyndProxy validated proxy pool

## Current pool

- Alive now: 432
- Gold now: 364
- HTTP: 66 alive / 41 gold
- HTTPS: 30 alive / 11 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 173 alive / 156 gold

## Historical pool

- Discovered: 173751
- Ever alive: 33023
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
