# SyndProxy private pool

## Current pool

- Alive now: 1059
- Gold now: 393
- HTTP: 348 alive / 90 gold
- HTTPS: 262 alive / 22 gold
- SOCKS4: 190 alive / 112 gold
- SOCKS5: 259 alive / 169 gold

## Historical pool

- Discovered: 166616
- Ever alive: 32445
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
