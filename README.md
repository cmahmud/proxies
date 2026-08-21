# SyndProxy private pool

## Current pool

- Alive now: 774
- Gold now: 407
- HTTP: 195 alive / 83 gold
- HTTPS: 124 alive / 20 gold
- SOCKS4: 218 alive / 153 gold
- SOCKS5: 237 alive / 151 gold

## Historical pool

- Discovered: 155683
- Ever alive: 29208
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
