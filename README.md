# SyndProxy validated proxy pool

## Current pool

- Alive now: 559
- Gold now: 345
- HTTP: 113 alive / 43 gold
- HTTPS: 100 alive / 9 gold
- SOCKS4: 160 alive / 152 gold
- SOCKS5: 186 alive / 141 gold

## Historical pool

- Discovered: 171031
- Ever alive: 32804
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
