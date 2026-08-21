# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 429
- HTTP: 317 alive / 88 gold
- HTTPS: 219 alive / 28 gold
- SOCKS4: 216 alive / 154 gold
- SOCKS5: 258 alive / 159 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30236
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
