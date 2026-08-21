# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 409
- HTTP: 224 alive / 84 gold
- HTTPS: 146 alive / 21 gold
- SOCKS4: 219 alive / 153 gold
- SOCKS5: 233 alive / 151 gold

## Historical pool

- Discovered: 155683
- Ever alive: 29210
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
