# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 291
- HTTP: 195 alive / 72 gold
- HTTPS: 36 alive / 19 gold
- SOCKS4: 130 alive / 65 gold
- SOCKS5: 182 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47819
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
