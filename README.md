# SyndProxy private pool

## Current pool

- Alive now: 940
- Gold now: 298
- HTTP: 297 alive / 33 gold
- HTTPS: 202 alive / 6 gold
- SOCKS4: 218 alive / 131 gold
- SOCKS5: 223 alive / 128 gold

## Historical pool

- Discovered: 102843
- Ever alive: 13202
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
