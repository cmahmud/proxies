# SyndProxy validated proxy pool

## Current pool

- Alive now: 456
- Gold now: 315
- HTTP: 175 alive / 79 gold
- HTTPS: 30 alive / 20 gold
- SOCKS4: 80 alive / 70 gold
- SOCKS5: 171 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47823
- Ever gold: 1495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
