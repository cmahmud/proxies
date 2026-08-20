# SyndProxy private pool

## Current pool

- Alive now: 792
- Gold now: 404
- HTTP: 192 alive / 80 gold
- HTTPS: 147 alive / 25 gold
- SOCKS4: 227 alive / 153 gold
- SOCKS5: 226 alive / 146 gold

## Historical pool

- Discovered: 150213
- Ever alive: 27033
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
