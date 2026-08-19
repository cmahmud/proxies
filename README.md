# SyndProxy private pool

## Current pool

- Alive now: 1099
- Gold now: 510
- HTTP: 395 alive / 141 gold
- HTTPS: 259 alive / 84 gold
- SOCKS4: 239 alive / 150 gold
- SOCKS5: 206 alive / 135 gold

## Historical pool

- Discovered: 119808
- Ever alive: 17958
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
