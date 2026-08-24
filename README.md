# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 434
- HTTP: 128 alive / 78 gold
- HTTPS: 69 alive / 25 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34142
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
