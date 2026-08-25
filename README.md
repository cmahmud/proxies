# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 419
- HTTP: 101 alive / 64 gold
- HTTPS: 91 alive / 23 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35559
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
