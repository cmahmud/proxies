# SyndProxy private pool

## Current pool

- Alive now: 992
- Gold now: 298
- HTTP: 381 alive / 66 gold
- HTTPS: 221 alive / 16 gold
- SOCKS4: 202 alive / 116 gold
- SOCKS5: 188 alive / 100 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15597
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
