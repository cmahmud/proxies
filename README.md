# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 392
- HTTP: 109 alive / 77 gold
- HTTPS: 46 alive / 14 gold
- SOCKS4: 165 alive / 151 gold
- SOCKS5: 178 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48199
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
