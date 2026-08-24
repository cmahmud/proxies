# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 404
- HTTP: 112 alive / 63 gold
- HTTPS: 65 alive / 17 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33694
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
