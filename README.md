# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 415
- HTTP: 92 alive / 68 gold
- HTTPS: 116 alive / 22 gold
- SOCKS4: 182 alive / 160 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42597
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
