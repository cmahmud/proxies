# SyndProxy validated proxy pool

## Current pool

- Alive now: 586
- Gold now: 398
- HTTP: 151 alive / 71 gold
- HTTPS: 65 alive / 14 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 198 alive / 159 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33289
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
