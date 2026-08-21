# SyndProxy private pool

## Current pool

- Alive now: 916
- Gold now: 420
- HTTP: 259 alive / 86 gold
- HTTPS: 192 alive / 20 gold
- SOCKS4: 227 alive / 161 gold
- SOCKS5: 238 alive / 153 gold

## Historical pool

- Discovered: 158244
- Ever alive: 30034
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
