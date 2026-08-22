# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 399
- HTTP: 251 alive / 85 gold
- HTTPS: 235 alive / 27 gold
- SOCKS4: 229 alive / 137 gold
- SOCKS5: 255 alive / 150 gold

## Historical pool

- Discovered: 164253
- Ever alive: 32111
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
