# SyndProxy private pool

## Current pool

- Alive now: 1124
- Gold now: 533
- HTTP: 419 alive / 157 gold
- HTTPS: 253 alive / 88 gold
- SOCKS4: 238 alive / 151 gold
- SOCKS5: 214 alive / 137 gold

## Historical pool

- Discovered: 119808
- Ever alive: 18013
- Ever gold: 706

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
