# SyndProxy private pool

## Current pool

- Alive now: 1226
- Gold now: 512
- HTTP: 440 alive / 168 gold
- HTTPS: 342 alive / 48 gold
- SOCKS4: 233 alive / 148 gold
- SOCKS5: 211 alive / 148 gold

## Historical pool

- Discovered: 125702
- Ever alive: 19680
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
