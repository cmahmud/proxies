# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 415
- HTTP: 98 alive / 70 gold
- HTTPS: 108 alive / 20 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41943
- Ever gold: 1344

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
