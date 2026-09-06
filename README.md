# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 397
- HTTP: 106 alive / 79 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 162 alive / 152 gold
- SOCKS5: 175 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48196
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
