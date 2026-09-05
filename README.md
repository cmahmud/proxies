# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 314
- HTTP: 226 alive / 81 gold
- HTTPS: 30 alive / 15 gold
- SOCKS4: 81 alive / 73 gold
- SOCKS5: 172 alive / 145 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47822
- Ever gold: 1495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
