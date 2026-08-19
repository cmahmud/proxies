# SyndProxy private pool

## Current pool

- Alive now: 991
- Gold now: 532
- HTTP: 338 alive / 163 gold
- HTTPS: 237 alive / 91 gold
- SOCKS4: 211 alive / 150 gold
- SOCKS5: 205 alive / 128 gold

## Historical pool

- Discovered: 123229
- Ever alive: 18985
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
