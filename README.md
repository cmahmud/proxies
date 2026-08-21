# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 392
- HTTP: 271 alive / 78 gold
- HTTPS: 181 alive / 19 gold
- SOCKS4: 197 alive / 133 gold
- SOCKS5: 235 alive / 162 gold

## Historical pool

- Discovered: 157410
- Ever alive: 29683
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
