# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 447
- HTTP: 119 alive / 84 gold
- HTTPS: 61 alive / 28 gold
- SOCKS4: 169 alive / 164 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43691
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
