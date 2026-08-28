# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 425
- HTTP: 112 alive / 78 gold
- HTTPS: 129 alive / 21 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 199 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42411
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
