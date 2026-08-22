# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 420
- HTTP: 312 alive / 78 gold
- HTTPS: 229 alive / 28 gold
- SOCKS4: 216 alive / 141 gold
- SOCKS5: 263 alive / 173 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32229
- Ever gold: 1176

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
