# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 463
- HTTP: 127 alive / 88 gold
- HTTPS: 100 alive / 37 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46983
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
