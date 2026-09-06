# SyndProxy validated proxy pool

## Current pool

- Alive now: 384
- Gold now: 292
- HTTP: 69 alive / 37 gold
- HTTPS: 27 alive / 8 gold
- SOCKS4: 146 alive / 132 gold
- SOCKS5: 142 alive / 115 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48324
- Ever gold: 1529

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
