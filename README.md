# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 344
- HTTP: 292 alive / 82 gold
- HTTPS: 243 alive / 29 gold
- SOCKS4: 197 alive / 138 gold
- SOCKS5: 195 alive / 95 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32516
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
