# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 375
- HTTP: 83 alive / 47 gold
- HTTPS: 47 alive / 12 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 187 alive / 159 gold

## Historical pool

- Discovered: 172309
- Ever alive: 32969
- Ever gold: 1220

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
