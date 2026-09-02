# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 433
- HTTP: 105 alive / 74 gold
- HTTPS: 104 alive / 22 gold
- SOCKS4: 178 alive / 165 gold
- SOCKS5: 189 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47603
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
