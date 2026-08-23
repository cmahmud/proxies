# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 374
- HTTP: 85 alive / 41 gold
- HTTPS: 42 alive / 12 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 199 alive / 162 gold

## Historical pool

- Discovered: 172323
- Ever alive: 32984
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
