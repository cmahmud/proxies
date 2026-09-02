# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 444
- HTTP: 144 alive / 77 gold
- HTTPS: 120 alive / 28 gold
- SOCKS4: 184 alive / 165 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47621
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
