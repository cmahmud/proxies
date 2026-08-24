# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 425
- HTTP: 164 alive / 75 gold
- HTTPS: 82 alive / 21 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 203 alive / 167 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33874
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
