# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 439
- HTTP: 372 alive / 102 gold
- HTTPS: 226 alive / 28 gold
- SOCKS4: 206 alive / 143 gold
- SOCKS5: 254 alive / 166 gold

## Historical pool

- Discovered: 152769
- Ever alive: 28410
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
