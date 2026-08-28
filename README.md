# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 432
- HTTP: 138 alive / 80 gold
- HTTPS: 146 alive / 23 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42346
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
