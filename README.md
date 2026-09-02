# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 442
- HTTP: 99 alive / 76 gold
- HTTPS: 100 alive / 27 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 189 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47531
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
