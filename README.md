# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 416
- HTTP: 99 alive / 62 gold
- HTTPS: 86 alive / 21 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35595
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
