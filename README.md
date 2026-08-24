# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 406
- HTTP: 120 alive / 64 gold
- HTTPS: 50 alive / 17 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33673
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
