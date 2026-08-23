# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 391
- HTTP: 119 alive / 67 gold
- HTTPS: 54 alive / 14 gold
- SOCKS4: 161 alive / 152 gold
- SOCKS5: 208 alive / 158 gold

## Historical pool

- Discovered: 175458
- Ever alive: 33178
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
