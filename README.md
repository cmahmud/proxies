# SyndProxy private pool

## Current pool

- Alive now: 768
- Gold now: 409
- HTTP: 188 alive / 84 gold
- HTTPS: 148 alive / 23 gold
- SOCKS4: 209 alive / 156 gold
- SOCKS5: 223 alive / 146 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26979
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
