# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 405
- HTTP: 102 alive / 74 gold
- HTTPS: 51 alive / 21 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 183 alive / 158 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48096
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
