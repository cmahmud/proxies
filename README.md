# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 383
- HTTP: 98 alive / 63 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 178 alive / 154 gold
- SOCKS5: 181 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48110
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
