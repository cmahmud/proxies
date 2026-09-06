# SyndProxy validated proxy pool

## Current pool

- Alive now: 420
- Gold now: 306
- HTTP: 82 alive / 61 gold
- HTTPS: 33 alive / 13 gold
- SOCKS4: 150 alive / 121 gold
- SOCKS5: 155 alive / 111 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48382
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
