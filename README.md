# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 355
- HTTP: 331 alive / 71 gold
- HTTPS: 240 alive / 11 gold
- SOCKS4: 234 alive / 125 gold
- SOCKS5: 232 alive / 148 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20278
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
