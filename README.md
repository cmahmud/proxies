# SyndProxy private pool

## Current pool

- Alive now: 772
- Gold now: 401
- HTTP: 194 alive / 82 gold
- HTTPS: 149 alive / 24 gold
- SOCKS4: 215 alive / 151 gold
- SOCKS5: 214 alive / 144 gold

## Historical pool

- Discovered: 149523
- Ever alive: 27006
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
