# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 378
- HTTP: 225 alive / 70 gold
- HTTPS: 148 alive / 16 gold
- SOCKS4: 193 alive / 130 gold
- SOCKS5: 227 alive / 162 gold

## Historical pool

- Discovered: 148330
- Ever alive: 26043
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
