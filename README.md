# SyndProxy private pool

## Current pool

- Alive now: 874
- Gold now: 405
- HTTP: 232 alive / 94 gold
- HTTPS: 166 alive / 24 gold
- SOCKS4: 211 alive / 133 gold
- SOCKS5: 265 alive / 154 gold

## Historical pool

- Discovered: 154718
- Ever alive: 29028
- Ever gold: 1119

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
