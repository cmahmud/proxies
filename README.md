# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 426
- HTTP: 95 alive / 67 gold
- HTTPS: 96 alive / 26 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35683
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
