# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 380
- HTTP: 132 alive / 52 gold
- HTTPS: 42 alive / 9 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 190 alive / 162 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33451
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
