# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 384
- HTTP: 87 alive / 58 gold
- HTTPS: 61 alive / 15 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 170 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43403
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
