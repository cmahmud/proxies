# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 479
- HTTP: 381 alive / 127 gold
- HTTPS: 261 alive / 76 gold
- SOCKS4: 212 alive / 122 gold
- SOCKS5: 211 alive / 154 gold

## Historical pool

- Discovered: 119696
- Ever alive: 17880
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
