# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 427
- HTTP: 112 alive / 78 gold
- HTTPS: 121 alive / 19 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42437
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
