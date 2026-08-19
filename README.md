# SyndProxy private pool

## Current pool

- Alive now: 1150
- Gold now: 423
- HTTP: 372 alive / 90 gold
- HTTPS: 260 alive / 13 gold
- SOCKS4: 250 alive / 156 gold
- SOCKS5: 268 alive / 164 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20744
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
