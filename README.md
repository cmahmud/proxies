# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 395
- HTTP: 194 alive / 84 gold
- HTTPS: 135 alive / 22 gold
- SOCKS4: 218 alive / 148 gold
- SOCKS5: 223 alive / 141 gold

## Historical pool

- Discovered: 155683
- Ever alive: 29208
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
