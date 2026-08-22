# SyndProxy private pool

## Current pool

- Alive now: 891
- Gold now: 378
- HTTP: 245 alive / 87 gold
- HTTPS: 196 alive / 25 gold
- SOCKS4: 209 alive / 122 gold
- SOCKS5: 241 alive / 144 gold

## Historical pool

- Discovered: 164245
- Ever alive: 32064
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
