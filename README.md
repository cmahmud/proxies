# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 389
- HTTP: 114 alive / 58 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 175 alive / 154 gold
- SOCKS5: 188 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33522
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
