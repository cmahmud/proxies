# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 385
- HTTP: 101 alive / 65 gold
- HTTPS: 36 alive / 14 gold
- SOCKS4: 167 alive / 155 gold
- SOCKS5: 174 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48184
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
