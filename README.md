# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 383
- HTTP: 129 alive / 52 gold
- HTTPS: 64 alive / 12 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 199 alive / 162 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33378
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
