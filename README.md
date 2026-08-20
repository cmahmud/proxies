# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 422
- HTTP: 322 alive / 98 gold
- HTTPS: 260 alive / 28 gold
- SOCKS4: 245 alive / 150 gold
- SOCKS5: 256 alive / 146 gold

## Historical pool

- Discovered: 144747
- Ever alive: 25194
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
