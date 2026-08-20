# SyndProxy private pool

## Current pool

- Alive now: 870
- Gold now: 410
- HTTP: 238 alive / 90 gold
- HTTPS: 199 alive / 20 gold
- SOCKS4: 209 alive / 150 gold
- SOCKS5: 224 alive / 150 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27559
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
