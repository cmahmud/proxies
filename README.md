# SyndProxy validated proxy pool

## Current pool

- Alive now: 665
- Gold now: 415
- HTTP: 115 alive / 69 gold
- HTTPS: 184 alive / 19 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40634
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
