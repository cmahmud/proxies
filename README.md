# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 470
- HTTP: 136 alive / 91 gold
- HTTPS: 102 alive / 42 gold
- SOCKS4: 184 alive / 163 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46966
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
