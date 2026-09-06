# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 405
- HTTP: 104 alive / 76 gold
- HTTPS: 52 alive / 21 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 182 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48096
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
