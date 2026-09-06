# SyndProxy validated proxy pool

## Current pool

- Alive now: 461
- Gold now: 370
- HTTP: 81 alive / 55 gold
- HTTPS: 32 alive / 12 gold
- SOCKS4: 167 alive / 150 gold
- SOCKS5: 181 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48268
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
