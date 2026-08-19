# SyndProxy private pool

## Current pool

- Alive now: 1147
- Gold now: 405
- HTTP: 375 alive / 78 gold
- HTTPS: 227 alive / 14 gold
- SOCKS4: 275 alive / 155 gold
- SOCKS5: 270 alive / 158 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20691
- Ever gold: 873

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
