# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 364
- HTTP: 150 alive / 78 gold
- HTTPS: 63 alive / 24 gold
- SOCKS4: 143 alive / 115 gold
- SOCKS5: 175 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47994
- Ever gold: 1507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
