# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 190
- HTTP: 192 alive / 38 gold
- HTTPS: 98 alive / 6 gold
- SOCKS4: 86 alive / 66 gold
- SOCKS5: 139 alive / 80 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32749
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
