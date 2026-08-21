# SyndProxy private pool

## Current pool

- Alive now: 1250
- Gold now: 418
- HTTP: 446 alive / 104 gold
- HTTPS: 323 alive / 29 gold
- SOCKS4: 234 alive / 152 gold
- SOCKS5: 247 alive / 133 gold

## Historical pool

- Discovered: 159263
- Ever alive: 30342
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
