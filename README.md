# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 427
- HTTP: 113 alive / 78 gold
- HTTPS: 124 alive / 19 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42437
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
