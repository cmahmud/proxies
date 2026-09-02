# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 437
- HTTP: 110 alive / 79 gold
- HTTPS: 96 alive / 21 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47585
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
