# SyndProxy private pool

## Current pool

- Alive now: 732
- Gold now: 341
- HTTP: 192 alive / 70 gold
- HTTPS: 142 alive / 16 gold
- SOCKS4: 212 alive / 139 gold
- SOCKS5: 186 alive / 116 gold

## Historical pool

- Discovered: 145545
- Ever alive: 25360
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
