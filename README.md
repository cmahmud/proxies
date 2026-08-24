# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 388
- HTTP: 109 alive / 52 gold
- HTTPS: 45 alive / 13 gold
- SOCKS4: 190 alive / 157 gold
- SOCKS5: 196 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33384
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
