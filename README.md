# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 415
- HTTP: 96 alive / 72 gold
- HTTPS: 123 alive / 21 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 177 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41972
- Ever gold: 1346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
