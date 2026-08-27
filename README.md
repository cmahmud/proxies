# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 415
- HTTP: 100 alive / 74 gold
- HTTPS: 118 alive / 20 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 176 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41995
- Ever gold: 1347

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
