# SyndProxy private pool

## Current pool

- Alive now: 907
- Gold now: 366
- HTTP: 283 alive / 87 gold
- HTTPS: 198 alive / 18 gold
- SOCKS4: 200 alive / 124 gold
- SOCKS5: 226 alive / 137 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29833
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
