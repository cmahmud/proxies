# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 390
- HTTP: 100 alive / 50 gold
- HTTPS: 41 alive / 16 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 195 alive / 167 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33396
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
