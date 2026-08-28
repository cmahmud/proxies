# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 409
- HTTP: 108 alive / 75 gold
- HTTPS: 91 alive / 18 gold
- SOCKS4: 163 alive / 156 gold
- SOCKS5: 172 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43092
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
