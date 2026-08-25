# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 414
- HTTP: 109 alive / 65 gold
- HTTPS: 69 alive / 20 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35409
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
