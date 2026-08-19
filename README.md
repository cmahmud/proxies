# SyndProxy private pool

## Current pool

- Alive now: 1212
- Gold now: 413
- HTTP: 394 alive / 92 gold
- HTTPS: 299 alive / 20 gold
- SOCKS4: 237 alive / 141 gold
- SOCKS5: 282 alive / 160 gold

## Historical pool

- Discovered: 136183
- Ever alive: 22233
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
