# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 415
- HTTP: 95 alive / 66 gold
- HTTPS: 111 alive / 19 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42551
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
