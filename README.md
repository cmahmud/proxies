# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 382
- HTTP: 92 alive / 61 gold
- HTTPS: 36 alive / 17 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 169 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48164
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
