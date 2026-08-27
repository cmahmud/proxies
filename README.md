# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 420
- HTTP: 107 alive / 80 gold
- HTTPS: 113 alive / 18 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42079
- Ever gold: 1349

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
