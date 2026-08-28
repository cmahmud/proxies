# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 419
- HTTP: 114 alive / 76 gold
- HTTPS: 128 alive / 16 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42438
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
