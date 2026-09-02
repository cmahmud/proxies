# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 441
- HTTP: 98 alive / 75 gold
- HTTPS: 114 alive / 30 gold
- SOCKS4: 188 alive / 161 gold
- SOCKS5: 185 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47512
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
