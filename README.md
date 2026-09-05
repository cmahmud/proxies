# SyndProxy validated proxy pool

## Current pool

- Alive now: 385
- Gold now: 291
- HTTP: 108 alive / 74 gold
- HTTPS: 47 alive / 21 gold
- SOCKS4: 73 alive / 64 gold
- SOCKS5: 157 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47894
- Ever gold: 1501

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
