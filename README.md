# SyndProxy private pool

## Current pool

- Alive now: 831
- Gold now: 424
- HTTP: 241 alive / 93 gold
- HTTPS: 107 alive / 20 gold
- SOCKS4: 237 alive / 154 gold
- SOCKS5: 246 alive / 157 gold

## Historical pool

- Discovered: 157425
- Ever alive: 29752
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
