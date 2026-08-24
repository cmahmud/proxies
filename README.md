# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 390
- HTTP: 125 alive / 57 gold
- HTTPS: 55 alive / 11 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 199 alive / 164 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33373
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
