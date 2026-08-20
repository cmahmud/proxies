# SyndProxy private pool

## Current pool

- Alive now: 782
- Gold now: 350
- HTTP: 189 alive / 72 gold
- HTTPS: 175 alive / 19 gold
- SOCKS4: 207 alive / 133 gold
- SOCKS5: 211 alive / 126 gold

## Historical pool

- Discovered: 149501
- Ever alive: 26718
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
