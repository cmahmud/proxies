# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 396
- HTTP: 91 alive / 69 gold
- HTTPS: 31 alive / 13 gold
- SOCKS4: 173 alive / 153 gold
- SOCKS5: 183 alive / 161 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48243
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
