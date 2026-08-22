# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 387
- HTTP: 348 alive / 87 gold
- HTTPS: 223 alive / 24 gold
- SOCKS4: 186 alive / 113 gold
- SOCKS5: 254 alive / 163 gold

## Historical pool

- Discovered: 166621
- Ever alive: 32451
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
