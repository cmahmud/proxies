# SyndProxy private pool

## Current pool

- Alive now: 1067
- Gold now: 425
- HTTP: 348 alive / 80 gold
- HTTPS: 221 alive / 28 gold
- SOCKS4: 230 alive / 141 gold
- SOCKS5: 268 alive / 176 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32232
- Ever gold: 1176

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
