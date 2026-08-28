# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 394
- HTTP: 81 alive / 56 gold
- HTTPS: 99 alive / 15 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42935
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
