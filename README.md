# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 406
- HTTP: 234 alive / 86 gold
- HTTPS: 246 alive / 18 gold
- SOCKS4: 203 alive / 150 gold
- SOCKS5: 213 alive / 152 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27540
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
