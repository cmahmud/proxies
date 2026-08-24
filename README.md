# SyndProxy validated proxy pool

## Current pool

- Alive now: 615
- Gold now: 426
- HTTP: 160 alive / 75 gold
- HTTPS: 80 alive / 22 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 203 alive / 167 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33875
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
