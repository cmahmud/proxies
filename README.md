# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 431
- HTTP: 117 alive / 83 gold
- HTTPS: 67 alive / 29 gold
- SOCKS4: 160 alive / 156 gold
- SOCKS5: 174 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43656
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
