# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 415
- HTTP: 102 alive / 75 gold
- HTTPS: 104 alive / 19 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42038
- Ever gold: 1348

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
