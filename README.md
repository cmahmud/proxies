# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 447
- HTTP: 106 alive / 80 gold
- HTTPS: 103 alive / 31 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 186 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47376
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
