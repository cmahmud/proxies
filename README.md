# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 410
- HTTP: 106 alive / 75 gold
- HTTPS: 97 alive / 19 gold
- SOCKS4: 162 alive / 156 gold
- SOCKS5: 171 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43092
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
