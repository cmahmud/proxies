# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 412
- HTTP: 87 alive / 67 gold
- HTTPS: 105 alive / 17 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42583
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
