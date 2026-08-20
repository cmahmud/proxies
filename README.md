# SyndProxy private pool

## Current pool

- Alive now: 700
- Gold now: 371
- HTTP: 170 alive / 69 gold
- HTTPS: 135 alive / 18 gold
- SOCKS4: 201 alive / 147 gold
- SOCKS5: 194 alive / 137 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26207
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
