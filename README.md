# SyndProxy validated proxy pool

## Current pool

- Alive now: 473
- Gold now: 373
- HTTP: 78 alive / 42 gold
- HTTPS: 43 alive / 10 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 172852
- Ever alive: 32984
- Ever gold: 1221

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
