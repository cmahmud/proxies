# SyndProxy private pool

## Current pool

- Alive now: 994
- Gold now: 382
- HTTP: 314 alive / 80 gold
- HTTPS: 230 alive / 21 gold
- SOCKS4: 211 alive / 144 gold
- SOCKS5: 239 alive / 137 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32523
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
