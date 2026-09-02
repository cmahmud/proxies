# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 439
- HTTP: 139 alive / 74 gold
- HTTPS: 131 alive / 27 gold
- SOCKS4: 187 alive / 163 gold
- SOCKS5: 190 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47616
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
