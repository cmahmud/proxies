# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 416
- HTTP: 347 alive / 91 gold
- HTTPS: 235 alive / 36 gold
- SOCKS4: 228 alive / 142 gold
- SOCKS5: 241 alive / 147 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31720
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
