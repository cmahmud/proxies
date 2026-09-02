# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 439
- HTTP: 91 alive / 71 gold
- HTTPS: 110 alive / 30 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 187 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47461
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
