# SyndProxy validated proxy pool

## Current pool

- Alive now: 431
- Gold now: 334
- HTTP: 83 alive / 61 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 157 alive / 136 gold
- SOCKS5: 148 alive / 123 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48354
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
