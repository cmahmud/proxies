# SyndProxy private pool

## Current pool

- Alive now: 1240
- Gold now: 542
- HTTP: 461 alive / 185 gold
- HTTPS: 319 alive / 61 gold
- SOCKS4: 239 alive / 149 gold
- SOCKS5: 221 alive / 147 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19771
- Ever gold: 786

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
