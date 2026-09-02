# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 446
- HTTP: 91 alive / 73 gold
- HTTPS: 105 alive / 33 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 185 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47506
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
