# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 384
- HTTP: 127 alive / 71 gold
- HTTPS: 182 alive / 18 gold
- SOCKS4: 156 alive / 145 gold
- SOCKS5: 175 alive / 150 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39906
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
