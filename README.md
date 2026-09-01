# SyndProxy validated proxy pool

## Current pool

- Alive now: 672
- Gold now: 467
- HTTP: 136 alive / 95 gold
- HTTPS: 141 alive / 33 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 215 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46448
- Ever gold: 1444

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
