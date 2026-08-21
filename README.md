# SyndProxy private pool

## Current pool

- Alive now: 1111
- Gold now: 433
- HTTP: 365 alive / 110 gold
- HTTPS: 228 alive / 30 gold
- SOCKS4: 255 alive / 151 gold
- SOCKS5: 263 alive / 142 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30767
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
