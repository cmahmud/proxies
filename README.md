# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 394
- HTTP: 92 alive / 55 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 179378
- Ever alive: 33491
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
