# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 414
- HTTP: 97 alive / 69 gold
- HTTPS: 95 alive / 20 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35427
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
