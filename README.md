# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 393
- HTTP: 76 alive / 55 gold
- HTTPS: 49 alive / 18 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 175 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42804
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
