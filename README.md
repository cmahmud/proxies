# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 307
- HTTP: 258 alive / 59 gold
- HTTPS: 154 alive / 12 gold
- SOCKS4: 215 alive / 116 gold
- SOCKS5: 191 alive / 120 gold

## Historical pool

- Discovered: 129265
- Ever alive: 20147
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
