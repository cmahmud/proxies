# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 433
- HTTP: 98 alive / 74 gold
- HTTPS: 101 alive / 24 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47664
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
