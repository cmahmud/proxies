# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 414
- HTTP: 96 alive / 69 gold
- HTTPS: 91 alive / 20 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35427
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
