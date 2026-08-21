# SyndProxy private pool

## Current pool

- Alive now: 931
- Gold now: 400
- HTTP: 271 alive / 85 gold
- HTTPS: 183 alive / 22 gold
- SOCKS4: 221 alive / 146 gold
- SOCKS5: 256 alive / 147 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29111
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
