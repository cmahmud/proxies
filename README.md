# SyndProxy private pool

## Current pool

- Alive now: 638
- Gold now: 237
- HTTP: 163 alive / 36 gold
- HTTPS: 86 alive / 7 gold
- SOCKS4: 202 alive / 124 gold
- SOCKS5: 187 alive / 70 gold

## Historical pool

- Discovered: 94326
- Ever alive: 9354
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
