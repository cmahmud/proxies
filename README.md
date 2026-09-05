# SyndProxy validated proxy pool

## Current pool

- Alive now: 385
- Gold now: 303
- HTTP: 102 alive / 79 gold
- HTTPS: 57 alive / 23 gold
- SOCKS4: 72 alive / 67 gold
- SOCKS5: 154 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47917
- Ever gold: 1504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
