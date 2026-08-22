# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 393
- HTTP: 283 alive / 81 gold
- HTTPS: 237 alive / 25 gold
- SOCKS4: 207 alive / 146 gold
- SOCKS5: 241 alive / 141 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32524
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
