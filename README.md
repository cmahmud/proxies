# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 406
- HTTP: 81 alive / 58 gold
- HTTPS: 89 alive / 20 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42714
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
