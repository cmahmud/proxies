# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 383
- HTTP: 88 alive / 57 gold
- HTTPS: 62 alive / 11 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 175 alive / 160 gold

## Historical pool

- Discovered: 174836
- Ever alive: 33120
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
