# SyndProxy private pool

## Current pool

- Alive now: 847
- Gold now: 410
- HTTP: 199 alive / 86 gold
- HTTPS: 178 alive / 20 gold
- SOCKS4: 225 alive / 151 gold
- SOCKS5: 245 alive / 153 gold

## Historical pool

- Discovered: 151674
- Ever alive: 27573
- Ever gold: 1099

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
