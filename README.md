# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 419
- HTTP: 96 alive / 70 gold
- HTTPS: 106 alive / 21 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42528
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
