# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 395
- HTTP: 106 alive / 77 gold
- HTTPS: 41 alive / 17 gold
- SOCKS4: 173 alive / 151 gold
- SOCKS5: 177 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48201
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
