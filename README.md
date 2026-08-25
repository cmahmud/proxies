# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 422
- HTTP: 102 alive / 66 gold
- HTTPS: 94 alive / 21 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 194 alive / 174 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35742
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
