# SyndProxy private pool

## Current pool

- Alive now: 1087
- Gold now: 487
- HTTP: 414 alive / 162 gold
- HTTPS: 243 alive / 82 gold
- SOCKS4: 192 alive / 110 gold
- SOCKS5: 238 alive / 133 gold

## Historical pool

- Discovered: 123164
- Ever alive: 18763
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
