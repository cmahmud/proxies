# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 354
- HTTP: 326 alive / 79 gold
- HTTPS: 222 alive / 25 gold
- SOCKS4: 207 alive / 122 gold
- SOCKS5: 245 alive / 128 gold

## Historical pool

- Discovered: 165819
- Ever alive: 32331
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
