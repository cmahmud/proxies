# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 390
- HTTP: 116 alive / 55 gold
- HTTPS: 66 alive / 13 gold
- SOCKS4: 185 alive / 156 gold
- SOCKS5: 198 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33385
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
