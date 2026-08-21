# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 386
- HTTP: 358 alive / 98 gold
- HTTPS: 240 alive / 27 gold
- SOCKS4: 199 alive / 120 gold
- SOCKS5: 250 alive / 141 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28066
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
