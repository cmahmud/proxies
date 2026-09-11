# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 451
- HTTP: 131 alive / 91 gold
- HTTPS: 46 alive / 30 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49258
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
