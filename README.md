# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 446
- HTTP: 107 alive / 80 gold
- HTTPS: 104 alive / 30 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 186 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47376
- Ever gold: 1467

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
