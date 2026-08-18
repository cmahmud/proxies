# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 225
- HTTP: 297 alive / 30 gold
- HTTPS: 169 alive / 7 gold
- SOCKS4: 226 alive / 124 gold
- SOCKS5: 155 alive / 64 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13518
- Ever gold: 424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
