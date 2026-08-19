# SyndProxy private pool

## Current pool

- Alive now: 1039
- Gold now: 542
- HTTP: 376 alive / 165 gold
- HTTPS: 242 alive / 92 gold
- SOCKS4: 211 alive / 145 gold
- SOCKS5: 210 alive / 140 gold

## Historical pool

- Discovered: 123168
- Ever alive: 18794
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
