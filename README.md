# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 441
- HTTP: 87 alive / 71 gold
- HTTPS: 105 alive / 30 gold
- SOCKS4: 177 alive / 165 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47495
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
