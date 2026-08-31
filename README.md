# SyndProxy validated proxy pool

## Current pool

- Alive now: 690
- Gold now: 461
- HTTP: 143 alive / 89 gold
- HTTPS: 141 alive / 36 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 229 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45863
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
