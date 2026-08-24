# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 404
- HTTP: 120 alive / 62 gold
- HTTPS: 48 alive / 16 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33673
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
