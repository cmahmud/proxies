# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 443
- HTTP: 99 alive / 76 gold
- HTTPS: 108 alive / 28 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47531
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
