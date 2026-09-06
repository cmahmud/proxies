# SyndProxy validated proxy pool

## Current pool

- Alive now: 386
- Gold now: 300
- HTTP: 73 alive / 38 gold
- HTTPS: 27 alive / 10 gold
- SOCKS4: 145 alive / 135 gold
- SOCKS5: 141 alive / 117 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48324
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
