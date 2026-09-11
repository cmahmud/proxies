# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 439
- HTTP: 102 alive / 77 gold
- HTTPS: 46 alive / 29 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49164
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
