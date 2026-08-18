# SyndProxy private pool

## Current pool

- Alive now: 610
- Gold now: 212
- HTTP: 154 alive / 20 gold
- HTTPS: 80 alive / 9 gold
- SOCKS4: 166 alive / 98 gold
- SOCKS5: 210 alive / 85 gold

## Historical pool

- Discovered: 91520
- Ever alive: 8004
- Ever gold: 346

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
