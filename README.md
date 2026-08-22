# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 425
- HTTP: 297 alive / 86 gold
- HTTPS: 200 alive / 31 gold
- SOCKS4: 202 alive / 142 gold
- SOCKS5: 230 alive / 166 gold

## Historical pool

- Discovered: 163874
- Ever alive: 32022
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
