# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 468
- HTTP: 152 alive / 96 gold
- HTTPS: 137 alive / 32 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 213 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46294
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
