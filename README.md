# SyndProxy private pool

## Current pool

- Alive now: 1126
- Gold now: 265
- HTTP: 470 alive / 32 gold
- HTTPS: 187 alive / 5 gold
- SOCKS4: 232 alive / 121 gold
- SOCKS5: 237 alive / 107 gold

## Historical pool

- Discovered: 95406
- Ever alive: 11002
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
