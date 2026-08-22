# SyndProxy private pool

## Current pool

- Alive now: 1212
- Gold now: 411
- HTTP: 474 alive / 96 gold
- HTTPS: 288 alive / 26 gold
- SOCKS4: 214 alive / 142 gold
- SOCKS5: 236 alive / 147 gold

## Historical pool

- Discovered: 163250
- Ever alive: 31734
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
