# SyndProxy private pool

## Current pool

- Alive now: 1238
- Gold now: 510
- HTTP: 444 alive / 167 gold
- HTTPS: 343 alive / 47 gold
- SOCKS4: 225 alive / 148 gold
- SOCKS5: 226 alive / 148 gold

## Historical pool

- Discovered: 125702
- Ever alive: 19680
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
