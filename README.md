# SyndProxy private pool

## Current pool

- Alive now: 594
- Gold now: 217
- HTTP: 159 alive / 29 gold
- HTTPS: 82 alive / 7 gold
- SOCKS4: 157 alive / 98 gold
- SOCKS5: 196 alive / 83 gold

## Historical pool

- Discovered: 91718
- Ever alive: 8682
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
