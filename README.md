# SyndProxy private pool

## Current pool

- Alive now: 759
- Gold now: 348
- HTTP: 220 alive / 89 gold
- HTTPS: 133 alive / 25 gold
- SOCKS4: 175 alive / 107 gold
- SOCKS5: 231 alive / 127 gold

## Historical pool

- Discovered: 167408
- Ever alive: 32570
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
