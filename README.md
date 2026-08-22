# SyndProxy private pool

## Current pool

- Alive now: 1080
- Gold now: 387
- HTTP: 388 alive / 80 gold
- HTTPS: 218 alive / 27 gold
- SOCKS4: 227 alive / 145 gold
- SOCKS5: 247 alive / 135 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32526
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
