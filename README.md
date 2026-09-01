# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 468
- HTTP: 135 alive / 90 gold
- HTTPS: 109 alive / 37 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 200 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46354
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
