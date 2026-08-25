# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 417
- HTTP: 111 alive / 72 gold
- HTTPS: 104 alive / 21 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35053
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
