# SyndProxy private pool

## Current pool

- Alive now: 1179
- Gold now: 557
- HTTP: 400 alive / 173 gold
- HTTPS: 331 alive / 84 gold
- SOCKS4: 227 alive / 151 gold
- SOCKS5: 221 alive / 149 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19760
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
