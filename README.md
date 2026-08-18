# SyndProxy private pool

## Current pool

- Alive now: 749
- Gold now: 256
- HTTP: 233 alive / 29 gold
- HTTPS: 117 alive / 4 gold
- SOCKS4: 198 alive / 115 gold
- SOCKS5: 201 alive / 108 gold

## Historical pool

- Discovered: 99142
- Ever alive: 11913
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
