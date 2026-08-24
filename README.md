# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 423
- HTTP: 167 alive / 73 gold
- HTTPS: 107 alive / 20 gold
- SOCKS4: 185 alive / 162 gold
- SOCKS5: 193 alive / 168 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33863
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
