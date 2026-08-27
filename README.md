# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 417
- HTTP: 104 alive / 69 gold
- HTTPS: 133 alive / 18 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41331
- Ever gold: 1325

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
