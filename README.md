# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 366
- HTTP: 154 alive / 80 gold
- HTTPS: 63 alive / 25 gold
- SOCKS4: 143 alive / 114 gold
- SOCKS5: 175 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47990
- Ever gold: 1507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
