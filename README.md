# SyndProxy validated proxy pool

## Current pool

- Alive now: 596
- Gold now: 411
- HTTP: 148 alive / 70 gold
- HTTPS: 63 alive / 18 gold
- SOCKS4: 191 alive / 159 gold
- SOCKS5: 194 alive / 164 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33704
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
