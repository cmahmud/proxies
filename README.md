# SyndProxy private pool

## Current pool

- Alive now: 849
- Gold now: 227
- HTTP: 296 alive / 31 gold
- HTTPS: 166 alive / 8 gold
- SOCKS4: 231 alive / 124 gold
- SOCKS5: 156 alive / 64 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13518
- Ever gold: 424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
