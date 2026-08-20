# SyndProxy private pool

## Current pool

- Alive now: 676
- Gold now: 389
- HTTP: 168 alive / 70 gold
- HTTPS: 87 alive / 15 gold
- SOCKS4: 199 alive / 144 gold
- SOCKS5: 222 alive / 160 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25790
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
