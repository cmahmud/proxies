# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 406
- HTTP: 115 alive / 64 gold
- HTTPS: 53 alive / 16 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 181051
- Ever alive: 33669
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
