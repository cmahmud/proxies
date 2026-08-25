# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 427
- HTTP: 144 alive / 75 gold
- HTTPS: 86 alive / 25 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 195 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35181
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
