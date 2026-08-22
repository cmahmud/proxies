# SyndProxy private pool

## Current pool

- Alive now: 854
- Gold now: 435
- HTTP: 233 alive / 93 gold
- HTTPS: 172 alive / 25 gold
- SOCKS4: 208 alive / 151 gold
- SOCKS5: 241 alive / 166 gold

## Historical pool

- Discovered: 162754
- Ever alive: 31571
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
