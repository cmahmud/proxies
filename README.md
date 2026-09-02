# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 432
- HTTP: 95 alive / 74 gold
- HTTPS: 106 alive / 22 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47669
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
