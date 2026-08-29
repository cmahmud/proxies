# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 387
- HTTP: 90 alive / 62 gold
- HTTPS: 82 alive / 13 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 166 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43377
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
