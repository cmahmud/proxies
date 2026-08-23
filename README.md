# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 375
- HTTP: 84 alive / 48 gold
- HTTPS: 51 alive / 12 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 185 alive / 159 gold

## Historical pool

- Discovered: 172309
- Ever alive: 32969
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
