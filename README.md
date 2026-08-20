# SyndProxy private pool

## Current pool

- Alive now: 799
- Gold now: 392
- HTTP: 213 alive / 83 gold
- HTTPS: 168 alive / 20 gold
- SOCKS4: 204 alive / 136 gold
- SOCKS5: 214 alive / 153 gold

## Historical pool

- Discovered: 151050
- Ever alive: 27180
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
