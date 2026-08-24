# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 390
- HTTP: 108 alive / 52 gold
- HTTPS: 53 alive / 15 gold
- SOCKS4: 181 alive / 157 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33402
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
