# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 436
- HTTP: 97 alive / 78 gold
- HTTPS: 77 alive / 25 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47676
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
