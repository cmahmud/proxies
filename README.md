# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 379
- HTTP: 107 alive / 61 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 158 alive / 153 gold
- SOCKS5: 174 alive / 152 gold

## Historical pool

- Discovered: 176240
- Ever alive: 33202
- Ever gold: 1230

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
