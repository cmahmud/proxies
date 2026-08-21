# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 434
- HTTP: 338 alive / 88 gold
- HTTPS: 226 alive / 26 gold
- SOCKS4: 223 alive / 159 gold
- SOCKS5: 231 alive / 161 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29494
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
