# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 427
- HTTP: 118 alive / 77 gold
- HTTPS: 95 alive / 23 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34890
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
