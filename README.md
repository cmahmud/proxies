# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 452
- HTTP: 135 alive / 88 gold
- HTTPS: 99 alive / 33 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46986
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
