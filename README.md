# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 419
- HTTP: 88 alive / 70 gold
- HTTPS: 97 alive / 22 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42525
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
