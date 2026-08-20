# SyndProxy private pool

## Current pool

- Alive now: 716
- Gold now: 354
- HTTP: 178 alive / 71 gold
- HTTPS: 123 alive / 19 gold
- SOCKS4: 211 alive / 145 gold
- SOCKS5: 204 alive / 119 gold

## Historical pool

- Discovered: 145546
- Ever alive: 25369
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
