# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 424
- HTTP: 136 alive / 73 gold
- HTTPS: 100 alive / 24 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35195
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
