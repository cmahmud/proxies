# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 470
- HTTP: 134 alive / 91 gold
- HTTPS: 106 alive / 42 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46966
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
