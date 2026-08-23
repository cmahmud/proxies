# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 374
- HTTP: 81 alive / 42 gold
- HTTPS: 43 alive / 11 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 172852
- Ever alive: 32984
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
