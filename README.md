# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 391
- HTTP: 72 alive / 56 gold
- HTTPS: 74 alive / 12 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 170 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42929
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
