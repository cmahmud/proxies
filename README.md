# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 378
- HTTP: 86 alive / 65 gold
- HTTPS: 43 alive / 22 gold
- SOCKS4: 148 alive / 121 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48735
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
