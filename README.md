# SyndProxy validated proxy pool

## Current pool

- Alive now: 721
- Gold now: 29
- HTTP: 244 alive / 23 gold
- HTTPS: 96 alive / 2 gold
- SOCKS4: 111 alive / 0 gold
- SOCKS5: 270 alive / 4 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32668
- Ever gold: 1192

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
