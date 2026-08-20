# SyndProxy private pool

## Current pool

- Alive now: 807
- Gold now: 422
- HTTP: 196 alive / 80 gold
- HTTPS: 160 alive / 30 gold
- SOCKS4: 228 alive / 151 gold
- SOCKS5: 223 alive / 161 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27318
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
