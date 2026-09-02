# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 436
- HTTP: 113 alive / 80 gold
- HTTPS: 103 alive / 24 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47657
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
