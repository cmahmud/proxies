# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 404
- HTTP: 110 alive / 63 gold
- HTTPS: 49 alive / 16 gold
- SOCKS4: 174 alive / 157 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33669
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
