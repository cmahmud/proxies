# SyndProxy private pool

## Current pool

- Alive now: 1316
- Gold now: 598
- HTTP: 483 alive / 193 gold
- HTTPS: 359 alive / 100 gold
- SOCKS4: 233 alive / 147 gold
- SOCKS5: 241 alive / 158 gold

## Historical pool

- Discovered: 138957
- Ever alive: 23445
- Ever gold: 920

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
