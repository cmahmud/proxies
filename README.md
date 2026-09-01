# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 449
- HTTP: 99 alive / 75 gold
- HTTPS: 121 alive / 31 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 188 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47415
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
