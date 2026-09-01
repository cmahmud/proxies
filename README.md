# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 469
- HTTP: 130 alive / 90 gold
- HTTPS: 105 alive / 42 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46966
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
