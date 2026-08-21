# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 420
- HTTP: 304 alive / 84 gold
- HTTPS: 196 alive / 23 gold
- SOCKS4: 228 alive / 155 gold
- SOCKS5: 239 alive / 158 gold

## Historical pool

- Discovered: 159211
- Ever alive: 30214
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
