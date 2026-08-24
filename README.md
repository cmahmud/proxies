# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 387
- HTTP: 102 alive / 54 gold
- HTTPS: 47 alive / 10 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 194 alive / 163 gold

## Historical pool

- Discovered: 178001
- Ever alive: 33358
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
