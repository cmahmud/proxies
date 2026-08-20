# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 401
- HTTP: 194 alive / 80 gold
- HTTPS: 159 alive / 26 gold
- SOCKS4: 217 alive / 151 gold
- SOCKS5: 213 alive / 144 gold

## Historical pool

- Discovered: 149525
- Ever alive: 27019
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
