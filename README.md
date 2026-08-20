# SyndProxy private pool

## Current pool

- Alive now: 629
- Gold now: 356
- HTTP: 165 alive / 70 gold
- HTTPS: 92 alive / 22 gold
- SOCKS4: 184 alive / 123 gold
- SOCKS5: 188 alive / 141 gold

## Historical pool

- Discovered: 145817
- Ever alive: 25590
- Ever gold: 1067

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
