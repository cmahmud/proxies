# SyndProxy private pool

## Current pool

- Alive now: 1241
- Gold now: 493
- HTTP: 428 alive / 122 gold
- HTTPS: 326 alive / 71 gold
- SOCKS4: 226 alive / 150 gold
- SOCKS5: 261 alive / 150 gold

## Historical pool

- Discovered: 116452
- Ever alive: 17126
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
