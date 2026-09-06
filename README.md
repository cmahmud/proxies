# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 395
- HTTP: 104 alive / 79 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 169 alive / 151 gold
- SOCKS5: 177 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48201
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
