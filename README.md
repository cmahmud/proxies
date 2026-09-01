# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 433
- HTTP: 98 alive / 72 gold
- HTTPS: 123 alive / 33 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47306
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
