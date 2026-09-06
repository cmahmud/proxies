# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 384
- HTTP: 151 alive / 81 gold
- HTTPS: 58 alive / 24 gold
- SOCKS4: 156 alive / 129 gold
- SOCKS5: 185 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48010
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
