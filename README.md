# SyndProxy private pool

## Current pool

- Alive now: 792
- Gold now: 401
- HTTP: 200 alive / 82 gold
- HTTPS: 159 alive / 24 gold
- SOCKS4: 220 alive / 151 gold
- SOCKS5: 213 alive / 144 gold

## Historical pool

- Discovered: 149525
- Ever alive: 27015
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
