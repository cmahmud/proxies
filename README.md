# SyndProxy private pool

## Current pool

- Alive now: 1207
- Gold now: 495
- HTTP: 420 alive / 123 gold
- HTTPS: 303 alive / 70 gold
- SOCKS4: 225 alive / 152 gold
- SOCKS5: 259 alive / 150 gold

## Historical pool

- Discovered: 116452
- Ever alive: 17114
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
