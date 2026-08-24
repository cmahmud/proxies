# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 391
- HTTP: 109 alive / 54 gold
- HTTPS: 54 alive / 14 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 202 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33382
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
