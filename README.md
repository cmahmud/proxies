# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 398
- HTTP: 72 alive / 53 gold
- HTTPS: 47 alive / 18 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41683
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
