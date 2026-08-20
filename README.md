# SyndProxy private pool

## Current pool

- Alive now: 740
- Gold now: 369
- HTTP: 174 alive / 74 gold
- HTTPS: 129 alive / 23 gold
- SOCKS4: 214 alive / 147 gold
- SOCKS5: 223 alive / 125 gold

## Historical pool

- Discovered: 145546
- Ever alive: 25374
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
