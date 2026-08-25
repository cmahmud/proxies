# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 414
- HTTP: 95 alive / 65 gold
- HTTPS: 86 alive / 21 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35502
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
