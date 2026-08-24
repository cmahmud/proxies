# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 385
- HTTP: 123 alive / 55 gold
- HTTPS: 46 alive / 12 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33480
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
