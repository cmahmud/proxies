# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 439
- HTTP: 92 alive / 75 gold
- HTTPS: 104 alive / 28 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47515
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
