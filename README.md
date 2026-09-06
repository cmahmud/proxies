# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 409
- HTTP: 108 alive / 78 gold
- HTTPS: 59 alive / 18 gold
- SOCKS4: 168 alive / 152 gold
- SOCKS5: 182 alive / 161 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48093
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
