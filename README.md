# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 423
- HTTP: 106 alive / 65 gold
- HTTPS: 93 alive / 24 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 201 alive / 174 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35771
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
