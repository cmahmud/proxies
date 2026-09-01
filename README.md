# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 413
- HTTP: 104 alive / 64 gold
- HTTPS: 67 alive / 23 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47039
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
