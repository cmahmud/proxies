# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 346
- HTTP: 302 alive / 54 gold
- HTTPS: 185 alive / 14 gold
- SOCKS4: 240 alive / 138 gold
- SOCKS5: 240 alive / 140 gold

## Historical pool

- Discovered: 107067
- Ever alive: 14694
- Ever gold: 474

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
