# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 402
- HTTP: 89 alive / 56 gold
- HTTPS: 100 alive / 15 gold
- SOCKS4: 181 alive / 167 gold
- SOCKS5: 193 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41527
- Ever gold: 1336

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
