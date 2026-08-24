# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 384
- HTTP: 90 alive / 46 gold
- HTTPS: 55 alive / 14 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 188 alive / 164 gold

## Historical pool

- Discovered: 180329
- Ever alive: 33568
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
