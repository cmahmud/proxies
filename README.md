# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 303
- HTTP: 386 alive / 66 gold
- HTTPS: 224 alive / 18 gold
- SOCKS4: 199 alive / 116 gold
- SOCKS5: 179 alive / 103 gold

## Historical pool

- Discovered: 109990
- Ever alive: 15648
- Ever gold: 499

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
