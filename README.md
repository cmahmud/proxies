# SyndProxy private pool

## Current pool

- Alive now: 894
- Gold now: 393
- HTTP: 277 alive / 91 gold
- HTTPS: 190 alive / 14 gold
- SOCKS4: 224 alive / 158 gold
- SOCKS5: 203 alive / 130 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18238
- Ever gold: 717

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
