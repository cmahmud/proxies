# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 319
- HTTP: 221 alive / 81 gold
- HTTPS: 30 alive / 18 gold
- SOCKS4: 81 alive / 73 gold
- SOCKS5: 171 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47823
- Ever gold: 1495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
