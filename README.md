# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 431
- HTTP: 129 alive / 74 gold
- HTTPS: 80 alive / 25 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34602
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
