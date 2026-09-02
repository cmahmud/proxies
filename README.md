# SyndProxy validated proxy pool

## Current pool

- Alive now: 587
- Gold now: 435
- HTTP: 108 alive / 77 gold
- HTTPS: 104 alive / 23 gold
- SOCKS4: 184 alive / 162 gold
- SOCKS5: 191 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47580
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
