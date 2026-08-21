# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 421
- HTTP: 334 alive / 83 gold
- HTTPS: 205 alive / 26 gold
- SOCKS4: 243 alive / 155 gold
- SOCKS5: 237 alive / 157 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30209
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
