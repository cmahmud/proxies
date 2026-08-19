# SyndProxy private pool

## Current pool

- Alive now: 1275
- Gold now: 418
- HTTP: 446 alive / 96 gold
- HTTPS: 278 alive / 18 gold
- SOCKS4: 246 alive / 143 gold
- SOCKS5: 305 alive / 161 gold

## Historical pool

- Discovered: 131823
- Ever alive: 20949
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
