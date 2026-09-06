# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 389
- HTTP: 94 alive / 60 gold
- HTTPS: 37 alive / 16 gold
- SOCKS4: 181 alive / 156 gold
- SOCKS5: 177 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48161
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
