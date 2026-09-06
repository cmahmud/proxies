# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 401
- HTTP: 90 alive / 70 gold
- HTTPS: 32 alive / 14 gold
- SOCKS4: 167 alive / 153 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48243
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
