# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 415
- HTTP: 99 alive / 64 gold
- HTTPS: 110 alive / 23 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43001
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
