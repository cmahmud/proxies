# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 386
- HTTP: 88 alive / 60 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 183 alive / 157 gold
- SOCKS5: 180 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48153
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
