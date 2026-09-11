# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 405
- HTTP: 92 alive / 64 gold
- HTTPS: 37 alive / 21 gold
- SOCKS4: 169 alive / 149 gold
- SOCKS5: 184 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48812
- Ever gold: 1567

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
