# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 430
- HTTP: 123 alive / 78 gold
- HTTPS: 83 alive / 20 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33928
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
