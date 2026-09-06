# SyndProxy validated proxy pool

## Current pool

- Alive now: 457
- Gold now: 373
- HTTP: 80 alive / 56 gold
- HTTPS: 30 alive / 13 gold
- SOCKS4: 171 alive / 151 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48262
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
