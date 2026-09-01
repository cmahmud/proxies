# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 457
- HTTP: 128 alive / 85 gold
- HTTPS: 108 alive / 37 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 193 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46983
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
