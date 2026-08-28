# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 391
- HTTP: 71 alive / 49 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 176 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42856
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
