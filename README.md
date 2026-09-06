# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 404
- HTTP: 105 alive / 76 gold
- HTTPS: 57 alive / 19 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 177 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48094
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
