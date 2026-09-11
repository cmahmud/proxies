# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 439
- HTTP: 100 alive / 78 gold
- HTTPS: 46 alive / 29 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49166
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
