# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 452
- HTTP: 104 alive / 78 gold
- HTTPS: 105 alive / 31 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 192 alive / 180 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47420
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
