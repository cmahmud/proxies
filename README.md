# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 388
- HTTP: 144 alive / 82 gold
- HTTPS: 62 alive / 25 gold
- SOCKS4: 160 alive / 131 gold
- SOCKS5: 181 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48015
- Ever gold: 1511

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
