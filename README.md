# SyndProxy private pool

## Current pool

- Alive now: 1253
- Gold now: 550
- HTTP: 460 alive / 171 gold
- HTTPS: 358 alive / 84 gold
- SOCKS4: 225 alive / 147 gold
- SOCKS5: 210 alive / 148 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19756
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
