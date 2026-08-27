# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 419
- HTTP: 100 alive / 76 gold
- HTTPS: 108 alive / 17 gold
- SOCKS4: 183 alive / 158 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42113
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
