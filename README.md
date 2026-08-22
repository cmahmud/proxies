# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 420
- HTTP: 276 alive / 92 gold
- HTTPS: 194 alive / 29 gold
- SOCKS4: 216 alive / 144 gold
- SOCKS5: 259 alive / 155 gold

## Historical pool

- Discovered: 167127
- Ever alive: 32548
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
