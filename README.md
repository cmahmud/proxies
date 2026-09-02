# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 434
- HTTP: 107 alive / 74 gold
- HTTPS: 116 alive / 24 gold
- SOCKS4: 184 alive / 161 gold
- SOCKS5: 198 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47571
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
