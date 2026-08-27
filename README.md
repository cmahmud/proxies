# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 427
- HTTP: 112 alive / 79 gold
- HTTPS: 124 alive / 21 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42158
- Ever gold: 1352

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
