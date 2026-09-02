# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 436
- HTTP: 92 alive / 70 gold
- HTTPS: 98 alive / 28 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47461
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
