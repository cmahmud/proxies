# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 404
- HTTP: 112 alive / 62 gold
- HTTPS: 52 alive / 16 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33681
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
