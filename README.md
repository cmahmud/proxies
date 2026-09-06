# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 403
- HTTP: 104 alive / 73 gold
- HTTPS: 58 alive / 21 gold
- SOCKS4: 167 alive / 153 gold
- SOCKS5: 177 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48094
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
