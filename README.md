# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 391
- HTTP: 305 alive / 82 gold
- HTTPS: 217 alive / 25 gold
- SOCKS4: 213 alive / 146 gold
- SOCKS5: 243 alive / 138 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32525
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
