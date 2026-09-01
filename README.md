# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 443
- HTTP: 106 alive / 79 gold
- HTTPS: 80 alive / 31 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 182 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47012
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
