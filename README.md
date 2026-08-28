# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 420
- HTTP: 117 alive / 78 gold
- HTTPS: 138 alive / 17 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42312
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
