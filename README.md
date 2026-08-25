# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 425
- HTTP: 139 alive / 73 gold
- HTTPS: 93 alive / 23 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 193 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35138
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
