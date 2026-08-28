# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 415
- HTTP: 95 alive / 68 gold
- HTTPS: 117 alive / 23 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42595
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
