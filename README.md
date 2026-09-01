# SyndProxy validated proxy pool

## Current pool

- Alive now: 687
- Gold now: 467
- HTTP: 150 alive / 96 gold
- HTTPS: 134 alive / 32 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 223 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46290
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
