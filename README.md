# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 391
- HTTP: 98 alive / 69 gold
- HTTPS: 48 alive / 13 gold
- SOCKS4: 173 alive / 153 gold
- SOCKS5: 181 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48106
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
