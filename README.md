# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 395
- HTTP: 403 alive / 89 gold
- HTTPS: 264 alive / 37 gold
- SOCKS4: 203 alive / 132 gold
- SOCKS5: 220 alive / 137 gold

## Historical pool

- Discovered: 163249
- Ever alive: 31709
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
