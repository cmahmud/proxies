# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 404
- HTTP: 119 alive / 66 gold
- HTTPS: 51 alive / 16 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33665
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
