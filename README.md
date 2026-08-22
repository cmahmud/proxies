# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 451
- HTTP: 281 alive / 101 gold
- HTTPS: 161 alive / 26 gold
- SOCKS4: 221 alive / 159 gold
- SOCKS5: 247 alive / 165 gold

## Historical pool

- Discovered: 167121
- Ever alive: 32538
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
