# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 442
- HTTP: 96 alive / 78 gold
- HTTPS: 100 alive / 28 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 183 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47528
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
