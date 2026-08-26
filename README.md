# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 397
- HTTP: 139 alive / 74 gold
- HTTPS: 170 alive / 24 gold
- SOCKS4: 161 alive / 146 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40013
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
