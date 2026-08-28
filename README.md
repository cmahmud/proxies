# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 401
- HTTP: 96 alive / 73 gold
- HTTPS: 82 alive / 14 gold
- SOCKS4: 163 alive / 155 gold
- SOCKS5: 170 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43075
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
