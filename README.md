# SyndProxy private pool

## Current pool

- Alive now: 742
- Gold now: 364
- HTTP: 177 alive / 71 gold
- HTTPS: 125 alive / 19 gold
- SOCKS4: 217 alive / 146 gold
- SOCKS5: 223 alive / 128 gold

## Historical pool

- Discovered: 145546
- Ever alive: 25369
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
