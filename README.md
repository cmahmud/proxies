# SyndProxy private pool

## Current pool

- Alive now: 720
- Gold now: 250
- HTTP: 173 alive / 27 gold
- HTTPS: 153 alive / 8 gold
- SOCKS4: 185 alive / 112 gold
- SOCKS5: 209 alive / 103 gold

## Historical pool

- Discovered: 95261
- Ever alive: 10224
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
