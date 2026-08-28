# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 428
- HTTP: 120 alive / 81 gold
- HTTPS: 126 alive / 23 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42386
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
