# SyndProxy private pool

## Current pool

- Alive now: 1061
- Gold now: 549
- HTTP: 374 alive / 157 gold
- HTTPS: 254 alive / 107 gold
- SOCKS4: 222 alive / 150 gold
- SOCKS5: 211 alive / 135 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19913
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
