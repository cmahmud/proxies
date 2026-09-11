# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 422
- HTTP: 103 alive / 72 gold
- HTTPS: 35 alive / 17 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48969
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
