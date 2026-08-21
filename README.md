# SyndProxy private pool

## Current pool

- Alive now: 949
- Gold now: 413
- HTTP: 288 alive / 89 gold
- HTTPS: 211 alive / 20 gold
- SOCKS4: 217 alive / 155 gold
- SOCKS5: 233 alive / 149 gold

## Historical pool

- Discovered: 158244
- Ever alive: 30037
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
