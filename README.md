# SyndProxy validated proxy pool

## Current pool

- Alive now: 651
- Gold now: 469
- HTTP: 138 alive / 96 gold
- HTTPS: 122 alive / 33 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 208 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46296
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
