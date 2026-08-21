# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 420
- HTTP: 280 alive / 88 gold
- HTTPS: 207 alive / 26 gold
- SOCKS4: 226 alive / 156 gold
- SOCKS5: 232 alive / 150 gold

## Historical pool

- Discovered: 158244
- Ever alive: 30042
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
