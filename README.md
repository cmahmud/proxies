# SyndProxy private pool

## Current pool

- Alive now: 906
- Gold now: 404
- HTTP: 263 alive / 91 gold
- HTTPS: 162 alive / 18 gold
- SOCKS4: 225 alive / 136 gold
- SOCKS5: 256 alive / 159 gold

## Historical pool

- Discovered: 166610
- Ever alive: 32433
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
