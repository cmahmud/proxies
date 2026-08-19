# SyndProxy private pool

## Current pool

- Alive now: 1224
- Gold now: 552
- HTTP: 435 alive / 172 gold
- HTTPS: 350 alive / 81 gold
- SOCKS4: 229 alive / 150 gold
- SOCKS5: 210 alive / 149 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19758
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
