# SyndProxy private pool

## Current pool

- Alive now: 808
- Gold now: 408
- HTTP: 220 alive / 77 gold
- HTTPS: 166 alive / 23 gold
- SOCKS4: 212 alive / 154 gold
- SOCKS5: 210 alive / 154 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27395
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
