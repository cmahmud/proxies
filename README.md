# SyndProxy validated proxy pool

## Current pool

- Alive now: 427
- Gold now: 343
- HTTP: 79 alive / 58 gold
- HTTPS: 31 alive / 15 gold
- SOCKS4: 155 alive / 136 gold
- SOCKS5: 162 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48395
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
