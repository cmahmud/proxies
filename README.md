# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 391
- HTTP: 105 alive / 52 gold
- HTTPS: 54 alive / 15 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33400
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
