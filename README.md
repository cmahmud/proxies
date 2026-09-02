# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 441
- HTTP: 89 alive / 76 gold
- HTTPS: 106 alive / 28 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 187 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47516
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
