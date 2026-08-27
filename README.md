# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 402
- HTTP: 112 alive / 65 gold
- HTTPS: 167 alive / 16 gold
- SOCKS4: 169 alive / 155 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40583
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
