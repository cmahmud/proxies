# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 404
- HTTP: 337 alive / 92 gold
- HTTPS: 191 alive / 27 gold
- SOCKS4: 214 alive / 136 gold
- SOCKS5: 244 alive / 149 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32099
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
