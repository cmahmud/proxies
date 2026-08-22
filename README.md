# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 403
- HTTP: 325 alive / 85 gold
- HTTPS: 220 alive / 25 gold
- SOCKS4: 230 alive / 147 gold
- SOCKS5: 252 alive / 146 gold

## Historical pool

- Discovered: 165502
- Ever alive: 32279
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
