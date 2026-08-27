# SyndProxy validated proxy pool

## Current pool

- Alive now: 648
- Gold now: 415
- HTTP: 119 alive / 71 gold
- HTTPS: 174 alive / 19 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40539
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
