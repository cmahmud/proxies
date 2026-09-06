# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 384
- HTTP: 148 alive / 82 gold
- HTTPS: 55 alive / 23 gold
- SOCKS4: 156 alive / 128 gold
- SOCKS5: 184 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48009
- Ever gold: 1509

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
