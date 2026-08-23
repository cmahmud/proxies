# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 367
- HTTP: 78 alive / 41 gold
- HTTPS: 33 alive / 12 gold
- SOCKS4: 174 alive / 153 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 172855
- Ever alive: 32986
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
