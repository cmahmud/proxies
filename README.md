# SyndProxy private pool

## Current pool

- Alive now: 1049
- Gold now: 418
- HTTP: 383 alive / 82 gold
- HTTPS: 204 alive / 24 gold
- SOCKS4: 212 alive / 146 gold
- SOCKS5: 250 alive / 166 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29744
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
