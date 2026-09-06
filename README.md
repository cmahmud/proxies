# SyndProxy validated proxy pool

## Current pool

- Alive now: 432
- Gold now: 361
- HTTP: 68 alive / 52 gold
- HTTPS: 30 alive / 12 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 171 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48255
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
