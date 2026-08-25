# SyndProxy validated proxy pool

## Current pool

- Alive now: 568
- Gold now: 428
- HTTP: 120 alive / 77 gold
- HTTPS: 92 alive / 23 gold
- SOCKS4: 168 alive / 157 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34903
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
