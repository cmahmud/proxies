# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 463
- HTTP: 129 alive / 91 gold
- HTTPS: 133 alive / 36 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 220 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46470
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
