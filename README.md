# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 435
- HTTP: 100 alive / 71 gold
- HTTPS: 98 alive / 29 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 189 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47335
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
