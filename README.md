# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 365
- HTTP: 78 alive / 41 gold
- HTTPS: 43 alive / 10 gold
- SOCKS4: 176 alive / 151 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 172852
- Ever alive: 32984
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
