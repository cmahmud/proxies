# SyndProxy private pool

## Current pool

- Alive now: 750
- Gold now: 404
- HTTP: 203 alive / 84 gold
- HTTPS: 144 alive / 23 gold
- SOCKS4: 194 alive / 143 gold
- SOCKS5: 209 alive / 154 gold

## Historical pool

- Discovered: 151067
- Ever alive: 27405
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
