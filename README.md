# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 404
- HTTP: 331 alive / 80 gold
- HTTPS: 209 alive / 15 gold
- SOCKS4: 268 alive / 150 gold
- SOCKS5: 234 alive / 159 gold

## Historical pool

- Discovered: 131098
- Ever alive: 20514
- Ever gold: 867

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
