# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 398
- HTTP: 104 alive / 80 gold
- HTTPS: 46 alive / 16 gold
- SOCKS4: 170 alive / 152 gold
- SOCKS5: 178 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48201
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
