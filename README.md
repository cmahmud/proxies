# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 392
- HTTP: 110 alive / 78 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 179 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48199
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
