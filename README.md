# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 414
- HTTP: 110 alive / 65 gold
- HTTPS: 76 alive / 20 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35408
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
