# SyndProxy validated proxy pool

## Current pool

- Alive now: 475
- Gold now: 401
- HTTP: 92 alive / 64 gold
- HTTPS: 34 alive / 19 gold
- SOCKS4: 161 alive / 147 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48804
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
