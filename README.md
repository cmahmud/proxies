# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 445
- HTTP: 90 alive / 73 gold
- HTTPS: 102 alive / 33 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 186 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47506
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
