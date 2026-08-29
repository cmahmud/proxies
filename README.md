# SyndProxy validated proxy pool

## Current pool

- Alive now: 557
- Gold now: 448
- HTTP: 135 alive / 90 gold
- HTTPS: 57 alive / 30 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43671
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
