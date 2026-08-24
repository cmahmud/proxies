# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 403
- HTTP: 119 alive / 62 gold
- HTTPS: 51 alive / 16 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33674
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
