# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 373
- HTTP: 88 alive / 61 gold
- HTTPS: 71 alive / 13 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 171 alive / 144 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43435
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
