# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 382
- HTTP: 107 alive / 64 gold
- HTTPS: 47 alive / 14 gold
- SOCKS4: 167 alive / 151 gold
- SOCKS5: 173 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48170
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
