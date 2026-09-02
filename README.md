# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 434
- HTTP: 103 alive / 76 gold
- HTTPS: 97 alive / 21 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 184 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47585
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
