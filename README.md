# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 431
- HTTP: 118 alive / 83 gold
- HTTPS: 132 alive / 20 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42340
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
