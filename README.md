# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 383
- HTTP: 289 alive / 84 gold
- HTTPS: 240 alive / 26 gold
- SOCKS4: 227 alive / 160 gold
- SOCKS5: 222 alive / 113 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32520
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
