# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 403
- HTTP: 105 alive / 68 gold
- HTTPS: 178 alive / 19 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 195 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40602
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
