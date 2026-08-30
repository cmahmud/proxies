# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 446
- HTTP: 119 alive / 84 gold
- HTTPS: 64 alive / 28 gold
- SOCKS4: 168 alive / 163 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43691
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
