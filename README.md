# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 437
- HTTP: 122 alive / 80 gold
- HTTPS: 105 alive / 25 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47655
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
