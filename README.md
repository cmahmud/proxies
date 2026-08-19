# SyndProxy private pool

## Current pool

- Alive now: 1094
- Gold now: 460
- HTTP: 418 alive / 120 gold
- HTTPS: 251 alive / 75 gold
- SOCKS4: 203 alive / 140 gold
- SOCKS5: 222 alive / 125 gold

## Historical pool

- Discovered: 113546
- Ever alive: 16650
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
